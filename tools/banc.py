#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""Suivi du banc d'essai — validation explicite (méthode du 09/10/2026).

Le banc ne compare plus la proposition de l'agent à une annotation de référence. Il mesure si les
écritures proposées peuvent être **comprises puis validées, précisées ou refusées** par la personne
qui en a la responsabilité. Pour chaque cas de `banc/corpus.yaml` :
  · source du cas (et consigne de cadrage, s'il y en a une) : présente ? empreinte conforme ?
  · proposition : `<espace>/propositions/<dossier_id>.json` (ou `non_soumises/`) ; contrôle formel ;
  · examen : questions posées à l'agent d'explicitation et appréciation des réponses (utile,
    insuffisante, erronée) — journal joint à la décision, ou journal en cours à côté de la proposition ;
  · décision : avis par écriture (comprise et validée, précision demandée, refusée), décision, motif.
Espaces : `depot` (ce dépôt) ; `local` (dossier MRC du porteur, banc_pilote_C/). Sorties : `banc/SUIVI.md`
(public : pour un cas local, des comptes seulement, ni motif, ni montant, ni question) et, avec --mrc,
`<MRC>/banc_pilote_C/SUIVI_complet.md` (avec motifs et questions).
Usage : tools/banc.py [--mrc ~/Documents/Claude/Projects/MRC]
"""
import argparse, collections, hashlib, json, os, subprocess
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def recu(p):
    return json.loads(subprocess.run([os.path.join(ROOT, "tools", "mrc-check.sh"), p], capture_output=True, check=True).stdout)

def lire_journal(p):
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()] if p and os.path.exists(p) else []

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mrc", help="dossier MRC du porteur (cas locaux)")
    ap.add_argument("--sortie", default=os.path.join(ROOT, "banc", "SUIVI.md"))
    a = ap.parse_args()
    corpus = yaml.safe_load(open(os.path.join(ROOT, "banc", "corpus.yaml"), encoding="utf-8"))["cas"]
    tot = collections.Counter(); avis_tot = collections.Counter(); app_tot = collections.Counter()
    pub, loc, det = [], [], []
    for c in corpus:
        local = c.get("espace") == "local"
        base = os.path.expanduser(a.mrc) if local and a.mrc else (None if local else ROOT)
        espace = os.path.join(base, "banc_pilote_C") if local and base else ROOT
        did = c["dossier_id"]; synth = c["statut"] == "synthetique"
        src = "—"
        for k in ("source_cas", "consigne"):
            if c.get(k) and base:
                p = os.path.join(base, c[k]["chemin"])
                v = "absente" if not os.path.exists(p) else ("conforme" if hashlib.sha256(open(p, "rb").read()).hexdigest() == c[k]["sha256"] else "MODIFIÉE")
                src = v if src in ("—", "conforme") else src
                if k == "consigne" and v != "conforme": src = f"consigne {v}"
        prop = os.path.join(espace, "propositions", f"{did}.json")
        rep = os.path.join(espace, "registre", did)
        etat, motif, avis, journal, prov, controle = "sans_proposition", "", [], [], {}, "—"
        if base and os.path.exists(os.path.join(rep, "decision.json")):
            d = json.load(open(os.path.join(rep, "decision.json"), encoding="utf-8")); hv = d["lifecycle"]["human_validation"]
            etat, motif = hv["decision"], hv["motif"]; avis = (hv.get("examen") or {}).get("lignes", [])
            journal = lire_journal(os.path.join(rep, "journal.jsonl")); prov = d["lifecycle"]["proposal"].get("provenance", {})
            controle = d["lifecycle"]["formal_control"]["issue"]
        elif base and os.path.exists(prop):
            etat = "en_examen"; journal = lire_journal(os.path.splitext(prop)[0] + ".journal.jsonl")
            prov = json.load(open(prop, encoding="utf-8"))["lifecycle"]["proposal"].get("provenance", {}); controle = recu(prop)["statut"]
        elif base and os.path.exists(os.path.join(espace, "propositions", "non_soumises", f"{did}.json")):
            etat = "non_soumise"
        elif not base:
            etat = "non_lu"
        apps = collections.Counter(e.get("appreciation") or "non_appreciee" for e in journal)
        av = collections.Counter(x["avis"] for x in avis)
        if not synth and etat != "non_lu":
            tot[etat] += 1; avis_tot.update(av); app_tot.update(apps)
        modele = f"{prov.get('fournisseur', '—')} / {prov.get('modele', '—')}" if prov else "—"
        avs = " · ".join(f"{k} {v}" for k, v in sorted(av.items())) or "—"
        qs = f"{len(journal)}" + (f" ({', '.join(f'{k} {v}' for k, v in sorted(apps.items()))})" if journal else "")
        nom = f"{c['id']}{' *(synthétique)*' if synth else ''}"
        pub.append(f"| {nom} | {c['titre']} | {c['statut']} | {'local' if local else 'dépôt'} | {modele} | {controle} | {qs} | {avs} | {etat} |")
        loc.append(f"| {nom} | {c['titre']} | {src} | {modele} | {controle} | {qs} | {avs} | {etat} | {motif} |")
        if journal or avis:
            det += [f"### {c['id']}", ""] + [f"- Question {e['n']} ({e.get('appreciation') or 'non appréciée'}) : {e['question']}" for e in journal] \
                   + [f"- Avis sur `{x['ligne']}` : {x['avis']}" + (f" — {x['motif']}" if x.get("motif") else "") for x in avis] + [""]
    resume = ("**Totaux (hors cas synthétiques)** — dossiers : " + (" · ".join(f"{k.replace('_', ' ')} {v}" for k, v in sorted(tot.items())) or "aucun")
              + " ; écritures : " + (" · ".join(f"{k.replace('_', ' ')} {v}" for k, v in sorted(avis_tot.items())) or "aucune examinée")
              + " ; réponses de l'agent d'explicitation : " + (" · ".join(f"{k.replace('_', ' ')} {v}" for k, v in sorted(app_tot.items())) or "aucune"))
    entete = "<!-- Généré par tools/banc.py — NE PAS ÉDITER À LA MAIN -->"
    out = [entete, "# Banc d'essai du pilote C — suivi de la validation explicite", "",
           "*Ce que mesure le banc : si les écritures proposées peuvent être comprises puis validées, précisées ou refusées par la personne qui en a la responsabilité, avec l'aide d'une fiche de lecture et d'un agent d'explicitation. Cas locaux : comptes seulement ; pièces et produits au dépôt privé, ouvert à des vérificateurs désignés (décision D6).*", "",
           "| Cas | Titre | Instruction | Espace | Proposant | Contrôle formel | Questions posées | Avis par écriture | Décision |",
           "| --- | --- | --- | --- | --- | --- | --- | --- | --- |", *pub, "", resume, ""]
    open(a.sortie, "w", encoding="utf-8").write("\n".join(out)); print("\n".join(out))
    if a.mrc:
        outl = [entete, "# Banc d'essai du pilote C — suivi complet (local)", "",
                "| Cas | Titre | Source | Proposant | Contrôle formel | Questions | Avis par écriture | Décision | Motif |",
                "| --- | --- | --- | --- | --- | --- | --- | --- | --- |", *loc, "", resume, "", "## Questions et avis", "", *(det or ["- aucun"]), ""]
        p = os.path.join(os.path.expanduser(a.mrc), "banc_pilote_C", "SUIVI_complet.md")
        os.makedirs(os.path.dirname(p), exist_ok=True); open(p, "w", encoding="utf-8").write("\n".join(outl))
        print(f"\n(suivi complet : {p})")

if __name__ == "__main__":
    main()
