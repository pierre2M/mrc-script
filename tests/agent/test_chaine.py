#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""Phase 3 — essai de la chaîne agent → contrôle formel → validation humaine → registre.

Dans un dossier temporaire, avec deux clés d'essai distinctes (agent, validateur) :
  ok  1. l'agent (fournisseur `rejeu`) produit une proposition PROPOSEE, signée, avec provenance ;
  ok  2. le rejeu est déterministe : même entrée, même proposition (octet pour octet) ;
  ok  3. le validateur inscrit une décision `validee` ; `check_registre` passe ;
  ko  4. l'agent ne peut pas écrire dans `registre/` ;
  ko  5. une proposition modifiée après signature est refusée par le validateur ;
  ko  6. une décision signée avec la clé de l'agent est détectée par `check_registre` ;
  ko  7. un refus formel (E1) n'admet que `rejetee` ; `rejetee` est inscrit ;
  ko  8. des signataires partageant une clé sont détectés (R1) ;
  ok  9. l'agent d'explicitation répond (rejeu), le journal est joint à la décision, son empreinte concorde ;
  ko 10. une décision `validee` avec une écriture en précision demandée est refusée ;
  ko 11. une décision sans avis sur chaque écriture est refusée.
"""
import json, os, shutil, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
T = os.path.join(ROOT, "tests", "agent")
PY = sys.executable

def run(*args, ok=True):
    r = subprocess.run(list(args), capture_output=True, text=True, cwd=ROOT)
    if ok and r.returncode != 0: raise SystemExit(f"échec inattendu : {' '.join(args)}\n{r.stdout}{r.stderr}")
    return r

def cle(t, nom):
    p = os.path.join(t, nom)
    run("ssh-keygen", "-q", "-t", "ed25519", "-N", "", "-C", nom, "-f", p)
    return p, " ".join(open(p + ".pub").read().split()[:2])

def main():
    res = []
    def note(n, cond, msg):
        res.append(cond); print(("ok    " if cond else "ÉCHEC ") + f"{n}. {msg}")
    with tempfile.TemporaryDirectory() as t:
        ka, pa = cle(t, "agent"); kv, pv = cle(t, "validateur")
        sig = os.path.join(t, "signataires")
        open(sig, "w").write(f'agent-proposition namespaces="mrc-proposition" {pa}\nvalidateur-pm namespaces="mrc-validation" {pv}\n')
        prop, reg = os.path.join(t, "propositions"), os.path.join(t, "registre")
        agent = [PY, "agent/proposer.py", "--source", os.path.join(T, "sources", "riviere_synthetique.md"),
                 "--fournisseur", "rejeu", "--reponse", os.path.join(T, "reponses", "riviere_synthetique.txt"),
                 "--date", "2026-10-07", "--cle", ka]
        run(*agent, "--sortie", prop)
        p = os.path.join(prop, "agent-riviere-synthetique.json"); d = json.load(open(p))
        lc = d["lifecycle"]
        note(1, lc["proposal"]["statut"] == "PROPOSEE" and lc["formal_control"] is None and lc["human_validation"] is None
             and os.path.exists(p + ".sig") and len(lc["proposal"]["provenance"]["gabarit_sha256"]) == 64,
             "proposition PROPOSEE, signée, avec provenance")
        b1 = open(p, "rb").read(); run(*agent, "--sortie", prop)
        note(2, open(p, "rb").read() == b1, "rejeu déterministe")
        val = [PY, "tools/valider.py", "--signataires", sig, "--registre", reg, "--date", "2026-10-07"]
        AV = ["--avis", "a1=comprise_validee", "--avis", "b1=comprise_validee"]
        exp = [PY, "agent/expliquer.py", "--proposition", p, "--fournisseur", "rejeu", "--date", "2026-10-09",
               "--reponse", os.path.join(T, "reponses", "explication_riviere.txt"), "--question", "Que dit l'écriture a1 ?"]
        run(*exp)
        jr = os.path.splitext(p)[0] + ".journal.jsonl"
        run(PY, "agent/expliquer.py", "--proposition", p, "--apprecier", "1", "utile")
        r10 = run(*val, "--proposition", p, "--decision", "validee", "--motif", "essai", "--cle", kv,
                  "--avis", "a1=comprise_validee", "--avis", "b1=precision_demandee", "--motif-ligne", "b1=montant à justifier", ok=False)
        r11 = run(*val, "--proposition", p, "--decision", "validee", "--motif", "essai", "--cle", kv, "--avis", "a1=comprise_validee", ok=False)
        run(*val, "--proposition", p, "--decision", "validee", "--motif", "essai", "--cle", kv, *AV, "--journal", jr)
        chk = [PY, "tools/check_registre.py", "--registre", reg, "--propositions", prop, "--signataires", sig]
        note(3, run(*chk, ok=False).returncode == 0, "décision validée inscrite ; check_registre passe")
        r = run(*agent, "--sortie", os.path.join(ROOT, "registre", "x"), ok=False)
        note(4, r.returncode != 0 and "registre" in (r.stdout + r.stderr), "l'agent ne peut pas écrire dans registre/")
        q = os.path.join(t, "falsifiee.json"); shutil.copy(p, q); shutil.copy(p + ".sig", q + ".sig")
        x = json.load(open(q)); x["registres"]["A"]["lignes"][0]["montant"]["valeur"] = 1; json.dump(x, open(q, "w"))
        r = run(*val, "--proposition", q, "--decision", "validee", "--motif", "essai", "--cle", kv, ok=False)
        note(5, r.returncode != 0 and "signature" in r.stderr, "proposition modifiée après signature refusée")
        reg2 = os.path.join(t, "registre2")
        run(PY, "tools/valider.py", "--signataires", sig, "--registre", reg2, "--date", "2026-10-07",
            "--proposition", p, "--decision", "validee", "--motif", "essai", "--cle", ka, *AV)
        r = run(PY, "tools/check_registre.py", "--registre", reg2, "--propositions", prop, "--signataires", sig, ok=False)
        note(6, r.returncode != 0 and "signature du validateur" in r.stdout, "décision signée par l'agent détectée")
        y = json.load(open(p)); y["dossier_id"] = "agent-sans-ancrage"; y["registres"]["B"]["ancrage"] = {}
        z = os.path.join(prop, "agent-sans-ancrage.json"); json.dump(y, open(z, "w"), ensure_ascii=False, indent=2)
        run("ssh-keygen", "-q", "-Y", "sign", "-f", ka, "-n", "mrc-proposition", z)
        r1 = run(*val, "--proposition", z, "--decision", "validee", "--motif", "essai", "--cle", kv, *AV, ok=False)
        r2 = run(*val, "--proposition", z, "--decision", "rejetee", "--motif", "C-01 : côté B sans ancrage", "--cle", kv,
                 "--avis", "a1=refusee", "--avis", "b1=refusee", "--motif-ligne", "a1=côté B non ancré", "--motif-ligne", "b1=côté B non ancré", ok=False)
        note(7, r1.returncode != 0 and r2.returncode == 0 and run(*chk, ok=False).returncode == 0,
             "refus formel : seule la décision rejetee est inscrite")
        sig2 = os.path.join(t, "signataires_partages")
        open(sig2, "w").write(f'agent-proposition namespaces="mrc-proposition" {pa}\nvalidateur-pm namespaces="mrc-validation" {pa}\n')
        r = run(PY, "tools/check_registre.py", "--registre", reg, "--propositions", prop, "--signataires", sig2, ok=False)
        note(8, r.returncode != 0 and "partagent une clé" in r.stdout, "clé partagée entre agent et validateur détectée")
        dj = json.load(open(os.path.join(reg, "agent-riviere-synthetique", "decision.json")))["lifecycle"]["human_validation"]["examen"]
        jj = open(os.path.join(reg, "agent-riviere-synthetique", "journal.jsonl")).read()
        note(9, dj.get("questions") == 1 and '"appreciation": "utile"' in jj and len(dj["fiche_sha256"]) == 64,
             "explicitation : journal joint (1 question, appréciée), fiche et journal empreintés")
        note(10, r10.returncode != 0 and "toutes les écritures" in r10.stderr, "validee refusée si une précision est demandée")
        note(11, r11.returncode != 0 and "un avis par écriture" in r11.stderr, "un avis par écriture est exigé")
    print(f"{sum(res)}/{len(res)} essais conformes")
    sys.exit(0 if all(res) else 1)

if __name__ == "__main__":
    main()
