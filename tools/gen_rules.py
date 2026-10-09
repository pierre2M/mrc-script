#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""Génère la forme machine du noyau démontré MRC v5.7 (rules/*.yaml).

Entrées (chemins passés en argument) :
  --noyau     NT-ARCH_v5.7_Noyau_demontre_ProfReg_2026-10-02.md
  --ntarch    MRC_v5.7_NT-ARCH_Architecture_Couches0-3.md (instantané figé)
  --profreg   racine du dépôt ProfReg (état de référence, identifié par son arbre git)
  --audit     journal d'audit (#print axioms)
  --out       dossier rules/
Aucune dépendance hors bibliothèque standard. Sortie déterministe.
"""
import argparse, glob, hashlib, json, os, re, subprocess

def q(x):  # chaîne YAML sûre (JSON est du YAML valide)
    return json.dumps(x, ensure_ascii=False)

def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()

ap = argparse.ArgumentParser()
for a in ('noyau', 'ntarch', 'profreg', 'audit', 'out'):
    ap.add_argument('--' + a, required=True)
A = ap.parse_args()

# 1. Théorèmes ProfReg : nom court -> module
mod = {}
for f in sorted(glob.glob(os.path.join(A.profreg, 'ProfReg', '*.lean'))):
    m = os.path.basename(f)[:-5]
    for t in re.findall(r"^\s*(?:theorem|lemma)\s+([A-Za-z0-9_'.]+)", open(f, encoding='utf-8').read(), re.M):
        mod.setdefault(t.split('.')[-1], m)
# 2. Axiomes Lean par théorème
ax = {}
for l in open(A.audit, encoding='utf-8'):
    m = re.match(r"'([^']+)' (does not depend on any axioms|depends on axioms: \[(.*)\])", l)
    if m:
        ax[m.group(1).split('.')[-1]] = [] if m.group(3) is None else [x.strip() for x in m.group(3).split(',')]
commit = subprocess.run(['git', '-C', A.profreg, 'rev-parse', 'HEAD^{tree}'], capture_output=True, text=True).stdout.strip()
# 3. Sections de NT-ARCH citant chaque théorème
nt = open(A.ntarch, encoding='utf-8').read().replace('\\_', '_').split('\n')
sec, cites = '', {}
for l in nt:
    h = re.match(r'^#{2,6} (.*)', l)
    if h:
        sec = re.split(r' [—-] ', h.group(1))[0].strip('* ')[:60]
    for t in set(re.findall(r"[A-Za-z][A-Za-z0-9_']*_[A-Za-z0-9_']*", l)):
        if t in mod:
            cites.setdefault(t, [])
            if sec not in cites[t]:
                cites[t].append(sec)
# 4. Lecture du noyau : lignes de tableau citant un théorème
noy = open(A.noyau, encoding='utf-8').read().split('\n')
heading, default_nat, theo, conv, axi, part = '', 'A', {}, [], [], ''
for l in noy:
    h = re.match(r'^(##+ |\*\*)(\d+(?:bis|ter)?(?:\.\d+(?:bis|ter)?)?)[. ]', l)
    if l.startswith('## '):
        heading = l[3:].strip(); part = heading.split('.')[0]
        default_nat = 'A'
    elif l.startswith('**10.'):
        heading = l.strip('* ').split('**')[0]
        default_nat = 'T' if heading.startswith('10.5') else 'A'
    if not l.startswith('|') or l.startswith('|---') or l.startswith('| ---'):
        continue
    cells = [c.strip() for c in l.strip('|').split('|')]
    if part.startswith('11') and cells[0].startswith('**AX-'):
        axi.append({'id': re.search(r'AX-\d+', cells[0]).group(0), 'intitule': re.sub(r'\*\*AX-\d+\*\*\s*—?\s*', '', cells[0]),
                    'enonce': cells[1], 'refutation': cells[2], 'theoremes': re.findall(r'`([A-Za-z0-9_]+)`', cells[3])})
        continue
    if part.startswith('12') and cells[0].startswith('**CONV-'):
        conv.append({"id": re.search(r"CONV-\d+", cells[0]).group(0), 'enonce': cells[1],
                     'ancrages': [t for t in re.findall(r'`([A-Za-z0-9_]+)`', cells[2]) if t in mod], 'rapport': cells[2]})
        continue
    names = [t for t in re.findall(r'`([A-Za-z0-9_]+)`', ' '.join(cells[1:2] or [''])) if t in mod]
    if not names:
        continue
    rest = ' '.join(cells[2:])
    nat = re.search(r'(?:^|\s|\*\*)([ATGL])(?:\*\*)?(?:\s|$|·)', ' '.join(cells[3:]) if len(cells) > 3 else '')
    nat = nat.group(1) if nat else ('L' if '(L)' in rest else 'A' if '(A)' in cells[0] else default_nat)
    if default_nat == 'T' and '(A)' in cells[0]:
        nat = 'A'
    rat = sorted(set(re.findall(r'(?:CONV|AX)-\d+', rest)))
    for n in names:
        theo.setdefault(n, {'enonce': re.sub(r'\s+', ' ', cells[0]), 'section_noyau': heading,
                            'nature': nat, 'rattachements': rat, 'nomme_par_ntarch': '⊕' not in cells[1]})
os.makedirs(A.out, exist_ok=True)
hdr = (f"# SPDX-License-Identifier: CC-BY-NC-SA-4.0\n# Généré par tools/gen_rules.py — NE PAS ÉDITER À LA MAIN\n"
       f"# noyau  sha256 {sha(A.noyau)}\n# ntarch sha256 {sha(A.ntarch)}\n"
       f"# profreg arbre  {commit}\n# audit  sha256 {sha(A.audit)}\n")
with open(os.path.join(A.out, 'theoremes.yaml'), 'w', encoding='utf-8') as o:
    o.write(hdr + f"mrc_release: \"v5.7\"\nprofreg_arbre: {q(commit)}\ntheoremes:\n")
    for n in sorted(theo, key=lambda k: (mod[k], k)):
        t = theo[n]
        o.write(f"  - id: {q(n)}\n    status: theorem\n    nature: {t['nature']}\n"
                f"    lean_ref: {{module: {q(mod[n])}, nom: {q(n)}, axiomes_lean: {q(ax.get(n, ['?']))}}}\n"
                f"    enonce: {q(t['enonce'])}\n    noyau_section: {q(t['section_noyau'])}\n"
                f"    ntarch_sections: {q(cites.get(n, []))}\n    nomme_par_ntarch: {str(t['nomme_par_ntarch']).lower()}\n"
                f"    rattachements: {q(t['rattachements'])}\n")
with open(os.path.join(A.out, 'conventions.yaml'), 'w', encoding='utf-8') as o:
    o.write(hdr + "conventions:\n")
    for c in conv:
        o.write(f"  - id: {q(c['id'])}\n    status: convention\n    enonce: {q(c['enonce'])}\n"
                f"    ancrages_profreg: {q(c['ancrages'])}\n    rapport_aux_theoremes: {q(c['rapport'])}\n")
with open(os.path.join(A.out, 'axiomes.yaml'), 'w', encoding='utf-8') as o:
    o.write(hdr + "axiomes:\n")
    for a in axi:
        o.write(f"  - id: {q(a['id'])}\n    status: axiom\n    intitule: {q(a['intitule'])}\n    enonce: {q(a['enonce'])}\n"
                f"    refutation: {q(a['refutation'])}\n    theoremes_lies: {q(a['theoremes'])}\n")
miss = [n for n in theo if n not in ax]
print(f"{len(theo)} théorèmes, {len(conv)} conventions, {len(axi)} axiomes ; sans axiome d'audit : {miss}")
