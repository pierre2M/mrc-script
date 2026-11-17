-- SPDX-License-Identifier: AGPL-3.0-only
-- Décision D7 (b), 07/10/2026 : ancrage de l'écriture duale élargi à deux teneurs quelconques.
-- Avant (PR-31 du 28/09, vérifié le 03/10) : `ancree ⟨tr, co, true⟩ = (tr.isSome && co.isSome)` —
-- traduction ET inscription de communalité exigées ensemble ; le couple banque / emprunteur était refusé.
-- Après : `ancreeDuale` (deux teneurs distincts, un ancrage déclaré par côté, de l'un ou l'autre type).
import ProfReg.PR31_BonneFormationDeclarative
import ProfReg.PR35_EcritureDuale
open ProfRegPR31

/-- Signature : l'ancrage d'une écriture duale est la conjonction « teneurs distincts ∧ A ancré ∧ B ancré ». -/
example (a b : CoteDuale) :
    ancreeDuale a b = (!(a.teneur == b.teneur) && ancree a.ancrage && ancree b.ancrage) := rfl

/-- Un côté est ancré par l'un OU l'autre ancrage. -/
example (tr co : Option Nat) : ancree ⟨tr, co⟩ = (tr.isSome || co.isSome) := rfl

/-- Les trois couples admis : deux comptabilités ; comptabilité et communalité ; deux registres de communalité. -/
example : ancreeDuale ⟨0, ⟨some 1, none⟩⟩ ⟨1, ⟨some 2, none⟩⟩ = true
    ∧ ancreeDuale ⟨0, ⟨some 1, none⟩⟩ ⟨1, ⟨none, some 2⟩⟩ = true
    ∧ ancreeDuale ⟨0, ⟨none, some 1⟩⟩ ⟨1, ⟨none, some 2⟩⟩ = true := by decide

/-- PR-31 et PR-35 concordent désormais sur le couple banque / emprunteur. -/
example : ProfRegPR35.EcritureDuale ProfRegPR35.registreBanque ProfRegPR35.registreEmprunteur
    ∧ ancreeDuale ⟨ProfRegPR35.banque, ⟨some 1, none⟩⟩ ⟨ProfRegPR35.emprunteur, ⟨some 2, none⟩⟩ = true :=
  ⟨ProfRegPR35.pret_bancaire_est_une_ecriture_duale, by decide⟩

#print axioms ancree_duale_ssi
#print axioms deux_comptabilites_tenues_ancrent_une_duale
