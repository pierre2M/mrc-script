-- SPDX-License-Identifier: AGPL-3.0-only
import MrcCheck

/-- `mrc-check <dossier.json> <contexte.json>` : écrit le reçu (JSON) sur la sortie standard.
    Code de sortie 0 dans tous les cas où un reçu est produit ; 2 si les fichiers sont illisibles. -/
def main (args : List String) : IO UInt32 := do
  match args with
  | [dossier, contexte] =>
    let ctxTxt ← IO.FS.readFile contexte
    match Lean.Json.parse ctxTxt >>= MrcCheck.decContexte with
    | .error e => IO.eprintln s!"contexte illisible : {e}"; return 2
    | .ok c =>
      let d ← IO.FS.readFile dossier
      IO.println (MrcCheck.recu d c).pretty
      return 0
  | _ => IO.eprintln "usage : mrc-check <dossier.json> <contexte.json>"; return 2
