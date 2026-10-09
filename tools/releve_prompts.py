#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""Phase 3.2 — relevé mécanique des écarts entre les prompts v5.5 de pierre2M/mrc et le set v5.7 / rules/.

Usage : tools/releve_prompts.py --site <clone de pierre2M/mrc> --set <dossier MRC_v5.7> > docs/releve_prompts_v55_table.md
Identifiants extraits : R-*, C-*, G-*, constantes en MAJUSCULES_SOULIGNÉES, champs en minuscules_soulignées.
Comparaison insensible aux accents. Présence textuelle seulement : elle ne dit pas que le sens est le même.
"""
import argparse, glob, os, re, subprocess, unicodedata
FICHIERS = ["apps/web/src/lib/prompts/mrc-schema-full.ts", "apps/web/src/lib/prompts/mrc-schema-light.ts",
            "apps/web/src/lib/mrc-definition.ts"]
PILOTE_C = ["teneur", "rapprochement", "ancrage", "écriture duale", "instance de contrôle", "déclaration des concernés",
            "maintien", "triplet porteur", "contrepartie", "ProfReg"]
RX = r"\b(?:[RCG]-[A-ZÀ-Ý_0-9-]+[A-ZÀ-Ý0-9]|[A-ZÀ-Ý]{3,}(?:_[A-ZÀ-Ý0-9]+)+|[a-zà-ÿ]+(?:_[a-zà-ÿ0-9]+)+)\b"
def norm(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").replace("\\_", "_")
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--site", required=True); ap.add_argument("--set", required=True); a = ap.parse_args()
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    commit = subprocess.run(["git", "-C", a.site, "log", "-1", "--format=%h %cs"], capture_output=True, text=True).stdout.strip()
    src = {f: open(os.path.join(a.site, f), encoding="utf-8").read() for f in FICHIERS}
    ids = {}
    for f, t in src.items():
        for m in re.findall(RX, t):
            if not m.startswith("MRC_"): ids.setdefault(m, set()).add(os.path.basename(f))
    st = {os.path.basename(f)[9:-3]: norm(open(f, encoding="utf-8").read()) for f in sorted(glob.glob(os.path.join(a.set, "MRC_v5.7_*.md")))}
    rules = norm("".join(open(f, encoding="utf-8").read() for f in glob.glob(os.path.join(root, "rules", "**", "*.yaml"), recursive=True)))
    print(f"<!-- Généré par tools/releve_prompts.py — pierre2M/mrc {commit} ; set MRC v5.7 ({len(st)} fichiers) -->\n")
    print("| Identifiant (prompts v5.5) | Prompt(s) | Occurrences dans le set v5.7 | Dans `rules/` |\n| --- | --- | --- | --- |")
    absents = 0
    for k in sorted(ids, key=norm):
        p = re.compile(r"(?<![\w-])" + re.escape(norm(k)) + r"(?![\w-])")
        h = {f: len(p.findall(t)) for f, t in st.items()}; h = {f: n for f, n in h.items() if n}
        tot = sum(h.values()); absents += not tot
        cell = "**absent**" if not tot else f"{tot} ({', '.join(f'{f} {n}' for f, n in sorted(h.items(), key=lambda x: -x[1])[:3])})"
        print(f"| `{k}` | {', '.join(sorted(ids[k]))} | {cell} | {'oui' if p.search(rules) else 'non'} |")
    print(f"\n{len(ids)} identifiants ; {absents} absents du set v5.7.\n")
    print("| Notion du pilote C | Occurrences dans les prompts v5.5 |\n| --- | --- |")
    tout = norm(" ".join(src.values())).lower()
    for n in PILOTE_C: print(f"| {n} | {tout.count(norm(n).lower())} |")
if __name__ == "__main__": main()
