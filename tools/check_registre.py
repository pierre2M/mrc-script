#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""Phase 3 — invariants du registre pilote et des propositions (CI).

  R1  `governance/signataires_autorises` : l'agent (`agent-proposition`, espace `mrc-proposition`)
      et le validateur (`validateur-pm`, espace `mrc-validation`) ont des clés DISTINCTES ; l'agent
      n'est autorisé dans aucun autre espace de noms.
  R2  chaque `propositions/*.json` est au statut PROPOSEE, sans contrôle ni validation.
  R3  chaque `registre/<id>/decision.json` est signé par le validateur ; la proposition d'origine
      agent est signée par l'agent ; la décision est conforme au schéma ; son corps (hors cycle de vie
      et trace de règles) est celui de la proposition ; l'issue formelle concorde avec le reçu ;
      un refus formel n'est suivi que d'un rejet ; l'opposabilité reste non ouverte.
  R4  examen explicite : la décision porte un avis par écriture, cohérent avec elle (validee ⇒ toutes
      comprises et validées ; précision demandée ⇒ retournee) ; la fiche de lecture (`fiche.md`) et, s'il
      y a lieu, le journal des questions (`journal.jsonl`) sont joints et leurs empreintes concordent.
Usage : tools/check_registre.py [--registre registre] [--propositions propositions] [--signataires F]
"""
import argparse, glob, hashlib, json, os, re, subprocess, sys
import jsonschema

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ISSUE = {"FORMELLEMENT_INCOMPLETE": {"mal_forme"}, "CONTROLE_ECHOUE": {"refuse"},
         "CONTROLE_NON_APPLICABLE": {"en_attente"}, "FORMELLEMENT_BIEN_FORMEE": {"conforme", "conforme_marque"}}

def verifier(f, principal, ns, sig):
    with open(f, "rb") as x:
        return subprocess.run(["ssh-keygen", "-Y", "verify", "-f", sig, "-I", principal, "-n", ns, "-s", f + ".sig"],
                              stdin=x, capture_output=True).returncode == 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--registre", default=os.path.join(ROOT, "registre"))
    ap.add_argument("--propositions", default=os.path.join(ROOT, "propositions"))
    ap.add_argument("--signataires", default=os.path.join(ROOT, "governance", "signataires_autorises"))
    a = ap.parse_args()
    err = []
    lignes = [l.split() for l in open(a.signataires, encoding="utf-8") if l.strip() and not l.startswith("#")]
    cles = {}
    for l in lignes:
        ns = re.search(r'namespaces="([^"]+)"', " ".join(l))
        cles.setdefault(l[0], []).append((ns.group(1) if ns else "*", l[-1]))
    ag, va = cles.get("agent-proposition", []), cles.get("validateur-pm", [])
    vide = not glob.glob(os.path.join(a.registre, "*", "")) and not glob.glob(os.path.join(a.propositions, "*.json"))
    if (not ag or not va) and not vide: err.append("R1 : agent-proposition et validateur-pm doivent être déclarés")
    if (not ag or not va) and vide: print("avertissement : aucune clé déclarée (registre et propositions vides)")
    if {k for _, k in ag} & {k for _, k in va}: err.append("R1 : l'agent et le validateur partagent une clé")
    if any(ns != "mrc-proposition" for ns, _ in ag): err.append("R1 : l'agent est autorisé hors de mrc-proposition")
    schema = json.load(open(os.path.join(ROOT, "schema", "ecriture_duale.schema.json"), encoding="utf-8"))
    val = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    for f in sorted(glob.glob(os.path.join(a.propositions, "*.json"))):
        lc = json.load(open(f, encoding="utf-8"))["lifecycle"]
        if lc["proposal"].get("statut") != "PROPOSEE" or lc.get("formal_control") or lc.get("human_validation"):
            err.append(f"R2 : {os.path.basename(f)} n'est pas une simple proposition")
    n = 0
    for rep in sorted(glob.glob(os.path.join(a.registre, "*", ""))):
        n += 1; i = os.path.basename(os.path.dirname(rep)); e = lambda m: err.append(f"R3 {i} : {m}")
        dp, pp, rp = (os.path.join(rep, x) for x in ("decision.json", "proposition.json", "recu.json"))
        if not all(map(os.path.exists, (dp, pp, rp, dp + ".sig"))): e("fichiers manquants"); continue
        if not verifier(dp, "validateur-pm", "mrc-validation", a.signataires): e("signature du validateur invalide")
        d, p, r = (json.load(open(x, encoding="utf-8")) for x in (dp, pp, rp))
        if p["lifecycle"]["proposal"].get("origine") == "agent" and not (
                os.path.exists(pp + ".sig") and verifier(pp, "agent-proposition", "mrc-proposition", a.signataires)):
            e("signature de l'agent absente ou invalide")
        if list(val.iter_errors(d)): e("décision non conforme au schéma")
        corps = lambda x: {k: v for k, v in x.items() if k not in ("lifecycle", "rule_trace")}
        if corps(d) != corps(p): e("le corps de la décision diffère de la proposition")
        if d["lifecycle"]["proposal"] != p["lifecycle"]["proposal"]: e("la proposition a été modifiée")
        iss = d["lifecycle"]["formal_control"]["issue"]
        if iss not in ISSUE.get(r["statut"], set()): e(f"issue {iss} incompatible avec le reçu {r['statut']}")
        if iss == "refuse" and d["lifecycle"]["human_validation"]["decision"] != "rejetee": e("refus formel non suivi d'un rejet")
        if d["lifecycle"]["opposability"]["statut"] != "non_ouverte": e("opposabilité ouverte")
        hv = d["lifecycle"]["human_validation"]; ex = hv.get("examen")
        if not ex: e("R4 : examen explicite absent"); continue
        ids = [l["id"] for c in ("A", "B") for l in d["registres"][c]["lignes"]]
        av = {x["ligne"]: x["avis"] for x in ex["lignes"]}
        if set(av) != set(ids): e("R4 : un avis par écriture est exigé")
        if hv["decision"] == "validee" and set(av.values()) - {"comprise_validee"}: e("R4 : validee sans que toutes les écritures soient validées")
        if "precision_demandee" in av.values() and hv["decision"] != "retournee" and iss != "refuse": e("R4 : précision demandée sans retour")
        fp = os.path.join(rep, "fiche.md")
        if not os.path.exists(fp) or hashlib.sha256(open(fp, "rb").read()).hexdigest() != ex["fiche_sha256"]: e("R4 : fiche de lecture absente ou modifiée")
        if "journal_sha256" in ex:
            jp = os.path.join(rep, "journal.jsonl")
            if not os.path.exists(jp) or hashlib.sha256(open(jp, "rb").read()).hexdigest() != ex["journal_sha256"]: e("R4 : journal absent ou modifié")
    for m in err: print("ÉCHEC", m)
    print(f"registre : {n} décision(s) ; {len(err)} écart(s)")
    sys.exit(1 if err else 0)

if __name__ == "__main__":
    main()
