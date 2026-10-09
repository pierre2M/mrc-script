#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""Agent de proposition du pilote C (phase 3.1).

Produit un dossier au statut `PROPOSEE` et rien d'autre :
  · le dossier est rédigé par un modèle à partir d'une source, selon `agent/gabarit_instructions.md` ;
  · le cycle de vie est imposé : `formal_control`, `human_validation` vides, opposabilité non ouverte ;
  · la provenance est complète : fournisseur, modèle, sha256 du gabarit, de l'entrée, de la réponse,
    du schéma et de `rules/` ;
  · le fichier est signé avec la clé de l'agent (espace de noms `mrc-proposition`), distincte de
    celle du validateur.
L'agent n'a aucun accès en écriture au registre : il n'écrit que dans le dossier de sortie, qui ne
peut pas être `registre/` ni l'un de ses sous-dossiers, et il n'importe aucun code du validateur.

Fournisseurs : `anthropic` (API Messages ; clé dans ANTHROPIC_API_KEY ; modèle obligatoire, sans
valeur par défaut) ; `rejeu` (réponse enregistrée : rejouable à l'identique, pour les tests et le banc).

Usage :
  agent/proposer.py --source S [--source S2 …] --fournisseur rejeu --reponse R.txt --cle ~/.ssh/mrc_agent
  agent/proposer.py --source S --fournisseur anthropic --modele <id> --enregistrer-reponse R.txt --cle …
"""
import argparse, datetime, glob, hashlib, json, os, re, subprocess, sys, urllib.error, urllib.request
import jsonschema, yaml

AGENT_VERSION = "mrc-agent/0.1"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRE = os.path.realpath(os.path.join(ROOT, "registre"))

def sha(b): return hashlib.sha256(b).hexdigest()
def sha_f(p): return sha(open(p, "rb").read())

def rules_sha():
    fs = sorted(glob.glob(os.path.join(ROOT, "rules", "**", "*.yaml"), recursive=True),
                key=lambda p: os.path.relpath(p, ROOT))
    return sha(b"".join(open(f, "rb").read() for f in fs))

def reference():
    man = open(os.path.join(ROOT, "corpus", "_MANIFESTE_v5.7.md"), encoding="utf-8").read()
    nt = re.search(r"([0-9a-f]{64})  MRC_v5\.7_NT-ARCH_Architecture_Couches0-3\.md", man).group(1)
    arbre = re.search(r"Arbre git \(local = publié\) \| `([0-9a-f]{40})`", man).group(1)
    return {"mrc_release": "v5.7", "ntarch_sha256": nt, "profreg_arbre": arbre}

def regles():
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, "rules", "pilote_C", "C-*.yaml"))):
        r = yaml.safe_load(open(f, encoding="utf-8"))
        eff = (r.get("defect_effect") or {})
        out.append(f"- **{r['id']} — {r['titre']}** ({r['status']}) : {r['enonce']}"
                   + (f" Défaut : {eff.get('code')} {eff.get('marqueur') or ''}".rstrip() if eff else ""))
    return "\n".join(out)

def contexte_tls():
    """Contexte TLS vérifié. Le Python de python.org sous macOS n'utilise pas les certificats du système :
    on prend ceux de `certifi` s'il est installé, sinon ceux de macOS (/etc/ssl/cert.pem). Jamais sans vérification."""
    import ssl
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        pass
    if os.path.exists("/etc/ssl/cert.pem"):
        return ssl.create_default_context(cafile="/etc/ssl/cert.pem")
    return ssl.create_default_context()

def appeler_anthropic(modele, prompt):
    cle = os.environ.get("ANTHROPIC_API_KEY")
    if not cle: sys.exit("ANTHROPIC_API_KEY absente")
    corps = json.dumps({"model": modele, "max_tokens": 8000,
                        "messages": [{"role": "user", "content": prompt}]}).encode()
    req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=corps, method="POST",
        headers={"x-api-key": cle, "anthropic-version": "2023-06-01", "content-type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=600, context=contexte_tls()) as r:
            rep = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"API Anthropic : erreur {e.code} — {e.read().decode(errors='replace')[:600]}")
    return "".join(b.get("text", "") for b in rep.get("content", []) if b.get("type") == "text")

def extraire_json(texte):
    i = texte.find("{")
    if i < 0: raise ValueError("aucun objet JSON dans la réponse")
    obj, _ = json.JSONDecoder().raw_decode(texte[i:])
    return obj

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", action="append", required=True)
    ap.add_argument("--sortie", default=os.path.join(ROOT, "propositions"))
    ap.add_argument("--fournisseur", choices=["anthropic", "rejeu"], required=True)
    ap.add_argument("--modele")
    ap.add_argument("--reponse", help="rejeu : réponse enregistrée")
    ap.add_argument("--enregistrer-reponse", help="anthropic : où enregistrer la réponse brute")
    ap.add_argument("--cle", help="clé privée SSH de l'agent (signature)")
    ap.add_argument("--sans-signature", action="store_true", help="essai local : la proposition ne sera pas recevable")
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    ap.add_argument("--auteur", default="agent de proposition")
    ap.add_argument("--dossier-id", help="identifiant imposé (banc d'essai : celui du cas dans banc/corpus.yaml)")
    a = ap.parse_args()

    sortie = os.path.realpath(a.sortie)
    if sortie == REGISTRE or sortie.startswith(REGISTRE + os.sep):
        sys.exit("refusé : l'agent n'écrit jamais dans registre/")
    if not a.cle and not a.sans_signature:
        sys.exit("--cle requise (ou --sans-signature pour un essai local)")

    gabarit_p = os.path.join(ROOT, "agent", "gabarit_instructions.md")
    schema_p = os.path.join(ROOT, "schema", "ecriture_duale.schema.json")
    schema = json.load(open(schema_p, encoding="utf-8"))
    entree = b"".join(f"=== {os.path.basename(s)} ===\n".encode() + open(s, "rb").read() + b"\n" for s in a.source)
    squelette = {"schema_version": "pilote-C/0.1", "reference": reference(),
                 "lifecycle": {"proposal": {"statut": "PROPOSEE", "auteur": a.auteur, "date": a.date, "origine": "agent"},
                               "formal_control": None, "human_validation": None,
                               "opposability": {"statut": "non_ouverte"}}}
    prompt = (open(gabarit_p, encoding="utf-8").read()
              .replace("{{REGLES}}", regles())
              .replace("{{SCHEMA}}", json.dumps(schema, ensure_ascii=False, indent=1))
              .replace("{{SQUELETTE}}", json.dumps(squelette, ensure_ascii=False, indent=1))
              .replace("{{SOURCE}}", entree.decode("utf-8", errors="replace")))

    if a.fournisseur == "rejeu":
        if not a.reponse: sys.exit("--reponse requise pour le rejeu")
        texte = open(a.reponse, encoding="utf-8").read(); modele = a.modele or "rejeu"
    else:
        if not a.modele: sys.exit("--modele requis (aucune valeur par défaut)")
        texte = appeler_anthropic(a.modele, prompt); modele = a.modele
        if a.enregistrer_reponse: open(a.enregistrer_reponse, "w", encoding="utf-8").write(texte)

    d = extraire_json(texte)
    # Squelette imposé : l'agent ne pose ni contrôle, ni validation, ni opposabilité, ni trace de règles.
    d.pop("rule_trace", None)
    d.update({"schema_version": squelette["schema_version"], "reference": squelette["reference"]})
    d.setdefault("dossier_id", "prop-" + sha(entree)[:12])
    if a.dossier_id: d["dossier_id"] = a.dossier_id
    lc = squelette["lifecycle"]
    lc["proposal"]["provenance"] = {"fournisseur": a.fournisseur, "modele": modele,
        "gabarit_sha256": sha_f(gabarit_p), "entree_sha256": sha(entree), "reponse_sha256": sha(texte.encode()),
        "schema_sha256": sha_f(schema_p), "rules_sha256": rules_sha(), "agent_version": AGENT_VERSION}
    d["lifecycle"] = lc
    texte_d = json.dumps(d, ensure_ascii=False, indent=2) + "\n"

    erreurs = [f"{list(e.absolute_path)} : {e.message}" for e in
               jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).iter_errors(d)]
    if erreurs:
        rep = os.path.join(sortie, "non_soumises"); os.makedirs(rep, exist_ok=True)
        p = os.path.join(rep, d["dossier_id"] + ".json")
        open(p, "w", encoding="utf-8").write(texte_d)
        open(p + ".erreurs.txt", "w", encoding="utf-8").write("\n".join(erreurs) + "\n")
        print(f"NON SOUMISE (schéma) : {p} — {len(erreurs)} erreur(s)", file=sys.stderr); sys.exit(3)

    os.makedirs(sortie, exist_ok=True)
    p = os.path.join(sortie, d["dossier_id"] + ".json")
    open(p, "w", encoding="utf-8").write(texte_d)
    if a.cle:
        if os.path.exists(p + ".sig"): os.remove(p + ".sig")
        subprocess.run(["ssh-keygen", "-q", "-Y", "sign", "-f", a.cle, "-n", "mrc-proposition", p],
                       check=True, capture_output=True)
    print(f"PROPOSEE : {p}" + ("" if a.cle else " (non signée)"))

if __name__ == "__main__":
    main()
