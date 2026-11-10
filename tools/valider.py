#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""Validation humaine et inscription au registre pilote (phase 3).

Seul ce script écrit dans `registre/`. Il est lancé par le validateur (règle D10 : P. M.), avec SA clé
(espace de noms `mrc-validation`), distincte de celle de l'agent. Il :
  1. vérifie la signature de la proposition quand elle vient de l'agent (principal `agent-proposition`,
     espace de noms `mrc-proposition`, fichier `governance/signataires_autorises`) ;
  2. lance le contrôle formel (`tools/mrc-check.sh`) et en tire `formal_control` et `rule_trace` ;
  3. refuse d'inscrire si le contrôle est impossible (`DONNEE_MANQUANTE`, `ECART_DE_VERSION`) ;
     n'admet que `rejetee` après un refus formel (E1) ;
  4. exige un **examen explicite** : la fiche de lecture (`tools/fiche.py`) est régénérée et son
     empreinte inscrite ; un avis par écriture (comprise_validee, precision_demandee, refusee) ; le
     journal des questions à l'agent d'explicitation, s'il y en a eu, est joint et son empreinte inscrite ;
     la décision doit être cohérente avec les avis ;
  5. écrit `registre/<dossier_id>/` : proposition (et sa signature), reçu, fiche, journal, décision,
     signature de la décision.
La décision ne rend rien opposable : `opposability.statut` reste `non_ouverte`.

Usage :
  tools/valider.py --proposition propositions/X.json --decision validee|retournee|rejetee \
                   --avis a1=comprise_validee --avis b1=precision_demandee --motif-ligne "b1=…" \
                   [--journal propositions/X.journal.jsonl] --motif "…" --cle ~/.ssh/mrc_validateur
"""
import argparse, datetime, hashlib, json, os, shutil, subprocess, sys
import jsonschema

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIGNATAIRES = os.path.join(ROOT, "governance", "signataires_autorises")
ISSUE = {"FORMELLEMENT_INCOMPLETE": "mal_forme", "CONTROLE_ECHOUE": "refuse", "CONTROLE_NON_APPLICABLE": "en_attente"}

def verifier(fichier, principal, ns, signataires):
    with open(fichier, "rb") as f:
        r = subprocess.run(["ssh-keygen", "-Y", "verify", "-f", signataires, "-I", principal, "-n", ns,
                            "-s", fichier + ".sig"], stdin=f, capture_output=True)
    return r.returncode == 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--proposition", required=True)
    ap.add_argument("--decision", choices=["validee", "retournee", "rejetee"], required=True)
    ap.add_argument("--motif", required=True)
    ap.add_argument("--cle", required=True, help="clé privée SSH du validateur")
    ap.add_argument("--validateur", default="P. M., porteur du registre pilote")
    ap.add_argument("--registre", default=os.path.join(ROOT, "registre"))
    ap.add_argument("--signataires", default=SIGNATAIRES)
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    ap.add_argument("--avis", action="append", default=[], help="<ligne>=comprise_validee|precision_demandee|refusee")
    ap.add_argument("--motif-ligne", action="append", default=[], help="<ligne>=<motif>")
    ap.add_argument("--journal", help="journal des questions à l'agent d'explicitation")
    a = ap.parse_args()

    p = json.load(open(a.proposition, encoding="utf-8"))
    pr = p["lifecycle"]["proposal"]
    if pr.get("statut") != "PROPOSEE" or p["lifecycle"].get("formal_control") or p["lifecycle"].get("human_validation"):
        sys.exit("refusé : le fichier n'est pas une proposition (statut PROPOSEE, sans contrôle ni validation)")
    if pr.get("origine") == "agent":
        if not os.path.exists(a.proposition + ".sig") or not verifier(a.proposition, "agent-proposition", "mrc-proposition", a.signataires):
            sys.exit("refusé : signature de l'agent absente ou invalide")

    recu_txt = subprocess.run([os.path.join(ROOT, "tools", "mrc-check.sh"), a.proposition],
                              capture_output=True, check=True).stdout
    recu = json.loads(recu_txt)
    st = recu["statut"]
    if st in ("DONNEE_MANQUANTE", "ECART_DE_VERSION"):
        sys.exit(f"contrôle impossible ({st} : {recu['motif']}) : rien n'est inscrit ; corriger et resoumettre")
    issue = ISSUE.get(st) or ("conforme_marque" if recu["effets"] else "conforme")
    if issue == "refuse" and a.decision != "rejetee":
        sys.exit("refusé : un refus formel (E1) n'admet que la décision `rejetee`")

    # Examen explicite : un avis par écriture, cohérent avec la décision.
    ids = [l["id"] for c in ("A", "B") for l in p["registres"][c]["lignes"]]
    avis = dict(x.split("=", 1) for x in a.avis); motifs = dict(x.split("=", 1) for x in a.motif_ligne)
    if set(avis) != set(ids):
        sys.exit(f"refusé : un avis par écriture est exigé ({', '.join(ids) or 'aucune écriture'}) ; reçus : {', '.join(avis) or 'aucun'}")
    if any(v not in ("comprise_validee", "precision_demandee", "refusee") for v in avis.values()):
        sys.exit("refusé : avis admis : comprise_validee, precision_demandee, refusee")
    if any(v != "comprise_validee" and not motifs.get(k) for k, v in avis.items()):
        sys.exit("refusé : une précision demandée ou un refus exige un motif (--motif-ligne <ligne>=…)")
    vals = set(avis.values())
    if a.decision == "validee" and vals - {"comprise_validee"}:
        sys.exit("refusé : `validee` exige que toutes les écritures soient comprises et validées")
    if "precision_demandee" in vals and a.decision != "retournee" and issue != "refuse":
        sys.exit("refusé : une précision demandée conduit à `retournee`")
    fiche = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "fiche.py"), a.proposition], capture_output=True, check=True).stdout
    examen = {"fiche_sha256": hashlib.sha256(fiche).hexdigest(),
              "lignes": [{"ligne": i, "avis": avis[i], **({"motif": motifs[i]} if motifs.get(i) else {})} for i in ids]}
    journal = open(a.journal, "rb").read() if a.journal else None
    if journal is not None:
        examen["journal_sha256"] = hashlib.sha256(journal).hexdigest()
        examen["questions"] = sum(1 for l in journal.decode().splitlines() if l.strip())
    d = json.loads(json.dumps(p))
    d["rule_trace"] = [{"regle": e["regle"], "resultat": "non_satisfaite", "effet": e["code"],
                        **({"marqueur": e["marqueur"]} if e.get("marqueur") else {})} for e in recu["effets"]]
    d["lifecycle"]["formal_control"] = {"issue": issue, "date": a.date,
        "outil": f"mrc-check/0.1 ; reçu sha256 {hashlib.sha256(recu_txt).hexdigest()}"}
    d["lifecycle"]["human_validation"] = {"decision": a.decision, "validateur": a.validateur, "date": a.date, "motif": a.motif,
                                          "examen": examen}
    schema = json.load(open(os.path.join(ROOT, "schema", "ecriture_duale.schema.json"), encoding="utf-8"))
    err = [e.message for e in jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).iter_errors(d)]
    if err: sys.exit("décision non conforme au schéma : " + " ; ".join(err[:3]))

    rep = os.path.join(a.registre, p["dossier_id"])
    if os.path.exists(rep): sys.exit(f"refusé : {rep} existe déjà (une décision n'est pas réécrite)")
    # Tout est préparé et signé dans un dossier provisoire, puis renommé : un échec (phrase de passe,
    # clé) ne laisse aucune décision incomplète dans le registre.
    tmp = rep + ".en_cours"
    if os.path.exists(tmp): shutil.rmtree(tmp)
    os.makedirs(tmp)
    try:
        shutil.copyfile(a.proposition, os.path.join(tmp, "proposition.json"))
        if os.path.exists(a.proposition + ".sig"):
            shutil.copyfile(a.proposition + ".sig", os.path.join(tmp, "proposition.json.sig"))
        open(os.path.join(tmp, "recu.json"), "wb").write(recu_txt)
        open(os.path.join(tmp, "fiche.md"), "wb").write(fiche)
        if journal is not None: open(os.path.join(tmp, "journal.jsonl"), "wb").write(journal)
        dp = os.path.join(tmp, "decision.json")
        open(dp, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
        r = subprocess.run(["ssh-keygen", "-q", "-Y", "sign", "-f", a.cle, "-n", "mrc-validation", dp],
                           stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
        if r.returncode != 0:
            raise RuntimeError("signature impossible (phrase de passe ou clé ?) : " + r.stderr.strip())
        os.rename(tmp, rep)
    except Exception as e:
        shutil.rmtree(tmp, ignore_errors=True)
        sys.exit(f"rien n'est inscrit — {e}")
    print(f"{a.decision.upper()} : {rep} (contrôle : {st}, issue {issue})")

if __name__ == "__main__":
    main()
