#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""Fiche de lecture d'un dossier proposé (validation explicite).

Rédige, SANS modèle de langage, un texte que la personne chargée de valider peut lire avant de
décider : qui inscrit quoi envers qui, sur quelle pièce ; ce que le contrôle formel a établi, en
mots ; ce qu'il ne vérifie pas ; les questions à se poser écriture par écriture. Le texte est
entièrement déterminé par le dossier, le reçu de `mrc-check` et les fiches de règles : même entrée,
même fiche (son sha256 est inscrit dans la décision).

Usage : tools/fiche.py <dossier.json> [--sortie fiche.md]      (empreinte sur stderr)
"""
import argparse, glob, hashlib, json, os, subprocess, sys
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NATURE = {"C+": "une **créance naît** (l'autre lui devra quelque chose)",
          "D+": "une **dette naît** (il devra quelque chose à l'autre)",
          "C-": "une **créance s'éteint** (ce que l'autre lui devait est réglé ou abandonné)",
          "D-": "une **dette s'éteint** (ce qu'il devait est réglé ou abandonné)"}
MIROIR = {"C+": "D+", "D+": "C+", "C-": "D-", "D-": "C-"}
STATUT = {"FORMELLEMENT_BIEN_FORMEE": "le dossier est **bien formé** : sa forme respecte les règles du pilote (éventuellement avec des marqueurs, ci-dessous).",
          "FORMELLEMENT_INCOMPLETE": "le dossier est **incomplet** : une condition de forme manque ; il peut être inscrit, mais marqué, ou renvoyé à la délibération.",
          "CONTROLE_ECHOUE": "le dossier est **refusé** au contrôle formel : il ne peut être que rejeté.",
          "CONTROLE_NON_APPLICABLE": "le contrôle **ne s'applique pas** à ce dossier (type non contrôlé, ou effet en attente).",
          "DONNEE_MANQUANTE": "le contrôle **n'a pas pu lire** le dossier (champ absent ou mal formé).",
          "ECART_DE_VERSION": "le dossier ne correspond **pas à l'état de référence** du modèle : à refaire."}
ECART = {"constate": "constaté (l'autre registre a été lu et ne porte pas le miroir)",
         "nonVerifiable": "non vérifiable (l'autre registre n'a pas été communiqué)",
         "refuse": "refusé (l'autre teneur refuse de communiquer)",
         "conteste": "contesté (l'autre registre porte une ligne contraire)"}

def nom(e, d):
    for c in ("A", "B"):
        if d["registres"][c]["teneur"] == e: return f"{e} (registre {c})"
    return e

def ancrage(r):
    a = r.get("ancrage", {})
    if "traduction_uri_ref" in a and "inscription_communalite_uri_ref" in a:
        return f"comptabilité tenue (`{a['traduction_uri_ref']}`) et registre de communalité"
    if "traduction_uri_ref" in a: return f"comptabilité tenue, référence déclarée `{a['traduction_uri_ref']}`"
    if "inscription_communalite_uri_ref" in a:
        i = a["inscription_communalite_uri_ref"]; return f"registre de communalité `{i.get('registre')}` de {i.get('entite')}"
    return "**aucun ancrage déclaré** (on ne sait pas où ce côté inscrit)"

MODE = {"arretee": "arrêtée par les concernés eux-mêmes", "ratifiee": "proposée par d'autres et seulement ratifiée par les concernés",
        "nonDeclare": "non déclarée"}

def milieu(r):
    m = r.get("registre_du_milieu")
    if not m: return []
    dc, mt = m["declaration"], m.get("maintien")
    out = [f"- Le registre B est celui d'un **{'milieu' if dc['nature'] == 'milieu' else 'collectif'}** : titulaire {dc['titulaire']}, "
           f"écrit par {dc['ecrivant']}, interprète {dc.get('interprete') or '**non désigné**'} ; déclaration des concernés "
           f"{MODE.get(dc['mode'], dc['mode'])}, {len(dc.get('concernes') or [])} concerné(s), critère d'inclusion "
           f"{'déclaré' if dc.get('inclusion') else '**absent**'}, réexamen {dc.get('reexamen') or '**non prévu**'}."]
    if mt:
        out.append(f"- Maintien déclaré : porté par {mt['porteur']}, envers {mt['contrepartie']}, dans le registre de {mt['registre']} ; "
                   f"{mt['situation']['du']} dus, {mt['situation']['paye']} engagés (le solde se calcule) ; horizon {mt['horizon']}.")
    else:
        out.append("- **Aucun maintien déclaré** pour ce registre.")
    return out

def instances(d):
    ds = d.get("designations_controle") or []
    m = {"arretee": "désignation arrêtée", "ratifiee": "désignation seulement ratifiée", "nonDeclare": "désignation non déclarée"}
    return [f"- Instance de contrôle : {x['registre']} désigne {x['instance']} ({m.get(x['mode'], x['mode'])})." for x in ds]

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("dossier"); ap.add_argument("--sortie"); a = ap.parse_args()
    d = json.load(open(a.dossier, encoding="utf-8"))
    r = json.loads(subprocess.run([os.path.join(ROOT, "tools", "mrc-check.sh"), a.dossier], capture_output=True, check=True).stdout)
    regles = {}
    for f in glob.glob(os.path.join(ROOT, "rules", "pilote_C", "C-*.yaml")):
        x = yaml.safe_load(open(f, encoding="utf-8")); regles[x["id"]] = x
    ev = {e["id"]: e for e in d.get("evidence", [])}
    A, B = d["registres"]["A"], d["registres"]["B"]
    pr = d["lifecycle"]["proposal"]; prov = pr.get("provenance", {})
    o = [f"# Fiche de lecture — dossier `{d['dossier_id']}`", "",
         "*Rédigée automatiquement, sans modèle de langage, à partir du dossier, du contrôle formel et des règles du pilote. Elle explique ; elle ne recommande aucune décision.*", "",
         "## 1. De quoi il s'agit", "",
         f"Deux registres sont mis en regard : celui de **{A['teneur']}** (registre A) et celui de **{B['teneur']}** (registre B). "
         f"Le registre A porte {len(A['lignes'])} écriture(s), le registre B {len(B['lignes'])}. "
         "Une *écriture duale* existe quand chaque écriture de l'un a son reflet chez l'autre : une créance d'un côté, la dette correspondante de l'autre.", "",
         f"- Registre A : {ancrage(A)}.", f"- Registre B : {ancrage(B)}.", *milieu(B), *instances(d), "",
         f"Proposé par : {pr['auteur']} ({pr['origine']}" + (f", modèle `{prov.get('modele')}`" if prov else "") + f"), le {pr['date']}.", "",
         "## 2. Les écritures proposées", ""]
    for c in ("A", "B"):
        R = d["registres"][c]
        for l in R["lignes"]:
            pieces = "; ".join(f"{p} — {ev[p]['ref']}" if p in ev else f"{p} (pièce non décrite)" for p in l.get("evidence", [])) or "**aucune pièce citée**"
            o += [f"### Écriture `{l['id']}` (registre {c})", "",
                  f"- **Ce qu'elle dit** : dans le registre de {R['teneur']}, {NATURE.get(l['typage'], l['typage'])} envers {nom(l['contrepartie'], d)}.",
                  f"- **Montant** : {l['montant']['valeur']:,} {l['montant']['valorimetre']}".replace(",", " ") + (f" — libellé : « {l['libelle']} »" if l.get("libelle") else ""),
                  f"- **Pièce(s)** : {pieces}",
                  f"- **Son reflet attendu** chez {l['contrepartie']} : une écriture `{MIROIR.get(l['typage'])}` envers {R['teneur']}.",
                  "- **À vous demander avant de valider** : la pièce dit-elle bien cela ? La contrepartie est-elle la bonne ? S'agit-il d'une naissance ou d'une extinction ? Le montant est-il celui de la pièce, et dans quelle unité ?", ""]
    if not A["lignes"] and not B["lignes"]:
        o += ["*Aucune écriture n'est proposée.*", ""]
    k = r.get("calculs") or {}
    o += ["## 3. Ce que le contrôle formel a établi", "", f"En résumé, {STATUT.get(r['statut'], r['statut'])}", ""]
    if r.get("motif"): o += [f"Motif : {r['motif']}", ""]
    er = k.get("etat_rapprochement")
    if er is not None:
        na, nb = len(er.get("A_vers_B") or []), len(er.get("B_vers_A") or [])
        o += [f"- **État de rapprochement** : {na} écriture(s) de A sans reflet chez B ; " +
              ("le registre B n'est pas pris en compte (voir les marqueurs)." if er.get("B_vers_A") is None else f"{nb} écriture(s) de B sans reflet chez A."),
              f"- **Écriture duale établie** : {'oui' if k.get('ecriture_duale') else 'non'}. " +
              ("Un écart n'est pas une faute de forme : il dit ce qui manque d'un côté ou de l'autre." if not k.get("ecriture_duale") else "")]
        for s in k.get("statut_ecart") or []:
            o.append(f"  - écart sur {s['ligne']['typage']} {s['ligne']['montant']} envers {s['ligne']['contrepartie']} : {ECART.get(s['statut'], s['statut'])}")
        if k.get("concordante") is False and k.get("ecriture_duale"):
            o.append("- Les montants des deux côtés diffèrent : l'écriture duale porte sur l'existence et le sens, pas sur la valeur.")
        o.append("")
    if r["effets"]:
        o += ["**Marqueurs et effets relevés :**", ""]
        for e in r["effets"]:
            x = regles.get(e["regle"], {})
            o.append(f"- **{e['regle']} — {x.get('titre', '')}** ({e['code']}, {e['effet']}) {e.get('marqueur') or ''} : {x.get('enonce', '')}")
        o.append("")
    o += ["## 4. Ce que le contrôle ne vérifie pas", "",
          "- Que les pièces existent et disent ce qu'on leur fait dire.", "- Que les montants sont exacts.",
          "- Que le typage (naissance ou extinction, créance ou dette) correspond à la réalité de l'opération.",
          "- Que les personnes ou organisations nommées acceptent d'être engagées.", ""]
    manques = []
    if not B["lignes"]: manques.append(f"Le registre B ({B['teneur']}) ne porte aucune écriture : son côté n'est pas documenté dans le dossier.")
    if B.get("communication") == "nonCommunique": manques.append("Le registre B n'a pas été communiqué : les écarts ne peuvent pas être vérifiés auprès de lui.")
    for c in ("A", "B"):
        for l in d["registres"][c]["lignes"]:
            if not l.get("evidence"): manques.append(f"L'écriture `{l['id']}` ne cite aucune pièce.")
    if manques: o += ["**Absences relevées dans ce dossier :**", "", *[f"- {m}" for m in manques], ""]
    o += ["## 5. Vos choix", "",
          "Pour chaque écriture : **comprise et validée**, **précision demandée** (au proposant), ou **refusée** (avec un motif). "
          "Vous pouvez interroger l'agent d'explicitation (`agent/expliquer.py`) ; vos questions et ses réponses sont jointes à votre décision. "
          "La validation n'efface aucun marqueur et ne rend rien opposable.", ""]
    txt = "\n".join(o)
    if a.sortie: open(a.sortie, "w", encoding="utf-8").write(txt)
    else: sys.stdout.write(txt)
    print(hashlib.sha256(txt.encode()).hexdigest(), file=sys.stderr)

if __name__ == "__main__":
    main()
