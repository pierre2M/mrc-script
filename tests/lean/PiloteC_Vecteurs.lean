-- SPDX-License-Identifier: AGPL-3.0-only
-- GÉNÉRÉ par tools/check_vectors.py — NE PAS ÉDITER À LA MAIN.
-- Chaque `example` fixe une valeur attendue d'un vecteur de tests/ ; `decide` l'établit
-- contre les définitions de ProfReg (arbre de référence : corpus/_MANIFESTE_v5.7.md). Identités encodées en `Nat`.

import ProfReg.PR31_BonneFormationDeclarative
import ProfReg.PR35_EcritureDuale
import ProfReg.PR37_RegistreDuMilieu
import ProfReg.PR40_StatutDeLEcart
import ProfReg.PR43_InstanceDeControle

namespace V_ko_01_sans_ancrage_B

def RA : ProfRegPR35.Registre Nat := ⟨0, [⟨1, .Cplus, 100⟩]⟩
def RB : ProfRegPR35.Registre Nat := ⟨1, [⟨0, .Dplus, 100⟩]⟩

-- C-01 ancrage par côté ; C-01 et C-02 ancrage de l'écriture duale (D7)
example : ProfRegPR31.ancree ⟨some 0, none⟩ = true := by decide
example : ProfRegPR31.ancree ⟨none, none⟩ = false := by decide
example : decide (RA.teneur ≠ RB.teneur) = true := by decide
example : ProfRegPR31.ancreeDuale ⟨0, ⟨some 0, none⟩⟩ ⟨1, ⟨none, none⟩⟩ = false := by decide

end V_ko_01_sans_ancrage_B

namespace V_ko_02_meme_teneur

def RA : ProfRegPR35.Registre Nat := ⟨0, [⟨0, .Cplus, 100⟩]⟩
def RB : ProfRegPR35.Registre Nat := ⟨0, [⟨0, .Dplus, 100⟩]⟩

-- C-01 ancrage par côté ; C-01 et C-02 ancrage de l'écriture duale (D7)
example : ProfRegPR31.ancree ⟨some 0, none⟩ = true := by decide
example : ProfRegPR31.ancree ⟨some 1, none⟩ = true := by decide
example : decide (RA.teneur ≠ RB.teneur) = false := by decide
example : ProfRegPR31.ancreeDuale ⟨0, ⟨some 0, none⟩⟩ ⟨0, ⟨some 1, none⟩⟩ = false := by decide

end V_ko_02_meme_teneur

namespace V_ko_04_riviere_ratifiee

def RA : ProfRegPR35.Registre Nat := ⟨0, [⟨1, .Dplus, 100⟩]⟩
def RB : ProfRegPR35.Registre Nat := ⟨1, [⟨0, .Cplus, 100⟩]⟩

-- C-01 ancrage par côté ; C-01 et C-02 ancrage de l'écriture duale (D7)
example : ProfRegPR31.ancree ⟨some 0, none⟩ = true := by decide
example : ProfRegPR31.ancree ⟨none, some 1⟩ = true := by decide
example : decide (RA.teneur ≠ RB.teneur) = true := by decide
example : ProfRegPR31.ancreeDuale ⟨0, ⟨some 0, none⟩⟩ ⟨1, ⟨none, some 1⟩⟩ = true := by decide

def decl : ProfRegPR37.DeclarationConcernes := ⟨1, .milieu, some 2, [3, 4], 5, some 2, .ratifiee, some 2030⟩
def mt : Option ProfRegPR37.MaintienMilieu := some ⟨5, 0, 1, ⟨100, 60⟩, 2030, 3⟩
def RBm : ProfRegPR37.RegistreDuMilieu Nat := ⟨decl, RB, rfl, mt⟩

-- C-07 déclaration des concernés ; C-08 maintien structuré
example : ProfRegPR37.declarationValide decl 2026 = false := by decide
example : (match mt with | some m => m.registre == decl.titulaire | none => false) = true := by decide
example : ProfRegPR37.bienForme RBm 2026 = false := by decide
example : mt.map ProfRegPR23.MaintienCONV11.solde = some 40 := by decide

-- C-04 (via PR-37) : colonne A = écart envers le titulaire
example : ProfRegPR37.ecartEnversMilieu 2026 RA 1 (some RBm) = [⟨1, .Dplus, 100⟩] := by decide
example : decide (ProfRegPR37.ecartEnversMilieu 2026 RA 1 (some RBm) = [] ∧ ProfRegPR37.bienForme RBm 2026 = true ∧ ProfRegPR35.ecart RB RA = []) = false := by decide

-- C-05 garde des deux silences
example : decide (ProfRegPR35.lignesVers RA RB = [] ∧ ProfRegPR35.lignesVers RB RA = []) = false := by decide

-- C-06 concordance (information)
example : decide (ProfRegPR35.Concordante RA RB) = true := by decide

-- C-10 instance de contrôle commune (CONV-16)
def ds : List ProfRegPR43.DesignationControle := [⟨0, 6, .arretee⟩, ⟨1, 6, .arretee⟩]
example : (ds.map (·.instanceCtrl)).any (ProfRegPR43.instanceCommune ds RA.teneur RB.teneur) = true := by decide

end V_ko_04_riviere_ratifiee

namespace V_ko_05_declaration_echue

def RA : ProfRegPR35.Registre Nat := ⟨0, [⟨1, .Dplus, 100⟩]⟩
def RB : ProfRegPR35.Registre Nat := ⟨1, [⟨0, .Cplus, 100⟩]⟩

-- C-01 ancrage par côté ; C-01 et C-02 ancrage de l'écriture duale (D7)
example : ProfRegPR31.ancree ⟨some 0, none⟩ = true := by decide
example : ProfRegPR31.ancree ⟨none, some 1⟩ = true := by decide
example : decide (RA.teneur ≠ RB.teneur) = true := by decide
example : ProfRegPR31.ancreeDuale ⟨0, ⟨some 0, none⟩⟩ ⟨1, ⟨none, some 1⟩⟩ = true := by decide

def decl : ProfRegPR37.DeclarationConcernes := ⟨1, .milieu, some 2, [3, 4], 5, some 2, .arretee, some 2030⟩
def mt : Option ProfRegPR37.MaintienMilieu := some ⟨5, 0, 1, ⟨100, 60⟩, 2030, 3⟩
def RBm : ProfRegPR37.RegistreDuMilieu Nat := ⟨decl, RB, rfl, mt⟩

-- C-07 déclaration des concernés ; C-08 maintien structuré
example : ProfRegPR37.declarationValide decl 2031 = false := by decide
example : (match mt with | some m => m.registre == decl.titulaire | none => false) = true := by decide
example : ProfRegPR37.bienForme RBm 2031 = false := by decide
example : mt.map ProfRegPR23.MaintienCONV11.solde = some 40 := by decide

-- C-04 (via PR-37) : colonne A = écart envers le titulaire
example : ProfRegPR37.ecartEnversMilieu 2031 RA 1 (some RBm) = [⟨1, .Dplus, 100⟩] := by decide
example : decide (ProfRegPR37.ecartEnversMilieu 2031 RA 1 (some RBm) = [] ∧ ProfRegPR37.bienForme RBm 2031 = true ∧ ProfRegPR35.ecart RB RA = []) = false := by decide

-- C-05 garde des deux silences
example : decide (ProfRegPR35.lignesVers RA RB = [] ∧ ProfRegPR35.lignesVers RB RA = []) = false := by decide

-- C-06 concordance (information)
example : decide (ProfRegPR35.Concordante RA RB) = true := by decide

-- C-10 instance de contrôle commune (CONV-16)
def ds : List ProfRegPR43.DesignationControle := [⟨0, 6, .arretee⟩, ⟨1, 6, .arretee⟩]
example : (ds.map (·.instanceCtrl)).any (ProfRegPR43.instanceCommune ds RA.teneur RB.teneur) = true := by decide

end V_ko_05_declaration_echue

namespace V_ko_06_milieu_ecrivant

def RA : ProfRegPR35.Registre Nat := ⟨0, [⟨1, .Dplus, 100⟩]⟩
def RB : ProfRegPR35.Registre Nat := ⟨1, [⟨0, .Cplus, 100⟩]⟩

-- C-01 ancrage par côté ; C-01 et C-02 ancrage de l'écriture duale (D7)
example : ProfRegPR31.ancree ⟨some 0, none⟩ = true := by decide
example : ProfRegPR31.ancree ⟨none, some 1⟩ = true := by decide
example : decide (RA.teneur ≠ RB.teneur) = true := by decide
example : ProfRegPR31.ancreeDuale ⟨0, ⟨some 0, none⟩⟩ ⟨1, ⟨none, some 1⟩⟩ = true := by decide

def decl : ProfRegPR37.DeclarationConcernes := ⟨1, .milieu, some 2, [3, 4], 1, some 2, .arretee, some 2030⟩
def mt : Option ProfRegPR37.MaintienMilieu := some ⟨5, 0, 1, ⟨100, 60⟩, 2030, 3⟩
def RBm : ProfRegPR37.RegistreDuMilieu Nat := ⟨decl, RB, rfl, mt⟩

-- C-07 déclaration des concernés ; C-08 maintien structuré
example : ProfRegPR37.declarationValide decl 2026 = false := by decide
example : (match mt with | some m => m.registre == decl.titulaire | none => false) = true := by decide
example : ProfRegPR37.bienForme RBm 2026 = false := by decide
example : mt.map ProfRegPR23.MaintienCONV11.solde = some 40 := by decide

-- C-04 (via PR-37) : colonne A = écart envers le titulaire
example : ProfRegPR37.ecartEnversMilieu 2026 RA 1 (some RBm) = [⟨1, .Dplus, 100⟩] := by decide
example : decide (ProfRegPR37.ecartEnversMilieu 2026 RA 1 (some RBm) = [] ∧ ProfRegPR37.bienForme RBm 2026 = true ∧ ProfRegPR35.ecart RB RA = []) = false := by decide

-- C-05 garde des deux silences
example : decide (ProfRegPR35.lignesVers RA RB = [] ∧ ProfRegPR35.lignesVers RB RA = []) = false := by decide

-- C-06 concordance (information)
example : decide (ProfRegPR35.Concordante RA RB) = true := by decide

-- C-10 instance de contrôle commune (CONV-16)
def ds : List ProfRegPR43.DesignationControle := [⟨0, 6, .arretee⟩, ⟨1, 6, .arretee⟩]
example : (ds.map (·.instanceCtrl)).any (ProfRegPR43.instanceCommune ds RA.teneur RB.teneur) = true := by decide

end V_ko_06_milieu_ecrivant

namespace V_ko_07_sans_maintien

def RA : ProfRegPR35.Registre Nat := ⟨0, [⟨1, .Dplus, 100⟩]⟩
def RB : ProfRegPR35.Registre Nat := ⟨1, [⟨0, .Cplus, 100⟩]⟩

-- C-01 ancrage par côté ; C-01 et C-02 ancrage de l'écriture duale (D7)
example : ProfRegPR31.ancree ⟨some 0, none⟩ = true := by decide
example : ProfRegPR31.ancree ⟨none, some 1⟩ = true := by decide
example : decide (RA.teneur ≠ RB.teneur) = true := by decide
example : ProfRegPR31.ancreeDuale ⟨0, ⟨some 0, none⟩⟩ ⟨1, ⟨none, some 1⟩⟩ = true := by decide

def decl : ProfRegPR37.DeclarationConcernes := ⟨1, .milieu, some 2, [3, 4], 5, some 2, .arretee, some 2030⟩
def mt : Option ProfRegPR37.MaintienMilieu := none
def RBm : ProfRegPR37.RegistreDuMilieu Nat := ⟨decl, RB, rfl, mt⟩

-- C-07 déclaration des concernés ; C-08 maintien structuré
example : ProfRegPR37.declarationValide decl 2026 = true := by decide
example : (match mt with | some m => m.registre == decl.titulaire | none => false) = false := by decide
example : ProfRegPR37.bienForme RBm 2026 = false := by decide
example : mt.map ProfRegPR23.MaintienCONV11.solde = none := by decide

-- C-04 (via PR-37) : colonne A = écart envers le titulaire
example : ProfRegPR37.ecartEnversMilieu 2026 RA 1 (some RBm) = [⟨1, .Dplus, 100⟩] := by decide
example : decide (ProfRegPR37.ecartEnversMilieu 2026 RA 1 (some RBm) = [] ∧ ProfRegPR37.bienForme RBm 2026 = true ∧ ProfRegPR35.ecart RB RA = []) = false := by decide

-- C-05 garde des deux silences
example : decide (ProfRegPR35.lignesVers RA RB = [] ∧ ProfRegPR35.lignesVers RB RA = []) = false := by decide

-- C-06 concordance (information)
example : decide (ProfRegPR35.Concordante RA RB) = true := by decide

-- C-10 instance de contrôle commune (CONV-16)
def ds : List ProfRegPR43.DesignationControle := [⟨0, 6, .arretee⟩, ⟨1, 6, .arretee⟩]
example : (ds.map (·.instanceCtrl)).any (ProfRegPR43.instanceCommune ds RA.teneur RB.teneur) = true := by decide

end V_ko_07_sans_maintien

namespace V_ko_08_maintien_autre_registre

def RA : ProfRegPR35.Registre Nat := ⟨0, [⟨1, .Dplus, 100⟩]⟩
def RB : ProfRegPR35.Registre Nat := ⟨1, [⟨0, .Cplus, 100⟩]⟩

-- C-01 ancrage par côté ; C-01 et C-02 ancrage de l'écriture duale (D7)
example : ProfRegPR31.ancree ⟨some 0, none⟩ = true := by decide
example : ProfRegPR31.ancree ⟨none, some 1⟩ = true := by decide
example : decide (RA.teneur ≠ RB.teneur) = true := by decide
example : ProfRegPR31.ancreeDuale ⟨0, ⟨some 0, none⟩⟩ ⟨1, ⟨none, some 1⟩⟩ = true := by decide

def decl : ProfRegPR37.DeclarationConcernes := ⟨1, .milieu, some 2, [3, 4], 5, some 2, .arretee, some 2030⟩
def mt : Option ProfRegPR37.MaintienMilieu := some ⟨5, 0, 0, ⟨100, 60⟩, 2030, 3⟩
def RBm : ProfRegPR37.RegistreDuMilieu Nat := ⟨decl, RB, rfl, mt⟩

-- C-07 déclaration des concernés ; C-08 maintien structuré
example : ProfRegPR37.declarationValide decl 2026 = true := by decide
example : (match mt with | some m => m.registre == decl.titulaire | none => false) = false := by decide
example : ProfRegPR37.bienForme RBm 2026 = false := by decide
example : mt.map ProfRegPR23.MaintienCONV11.solde = some 40 := by decide

-- C-04 (via PR-37) : colonne A = écart envers le titulaire
example : ProfRegPR37.ecartEnversMilieu 2026 RA 1 (some RBm) = [⟨1, .Dplus, 100⟩] := by decide
example : decide (ProfRegPR37.ecartEnversMilieu 2026 RA 1 (some RBm) = [] ∧ ProfRegPR37.bienForme RBm 2026 = true ∧ ProfRegPR35.ecart RB RA = []) = false := by decide

-- C-05 garde des deux silences
example : decide (ProfRegPR35.lignesVers RA RB = [] ∧ ProfRegPR35.lignesVers RB RA = []) = false := by decide

-- C-06 concordance (information)
example : decide (ProfRegPR35.Concordante RA RB) = true := by decide

-- C-10 instance de contrôle commune (CONV-16)
def ds : List ProfRegPR43.DesignationControle := [⟨0, 6, .arretee⟩, ⟨1, 6, .arretee⟩]
example : (ds.map (·.instanceCtrl)).any (ProfRegPR43.instanceCommune ds RA.teneur RB.teneur) = true := by decide

end V_ko_08_maintien_autre_registre

namespace V_ko_09_triplet_incomplet

def RA : ProfRegPR35.Registre Nat := ⟨0, [⟨1, .Dplus, 100⟩]⟩
def RB : ProfRegPR35.Registre Nat := ⟨1, [⟨0, .Cplus, 100⟩]⟩

-- C-01 ancrage par côté ; C-01 et C-02 ancrage de l'écriture duale (D7)
example : ProfRegPR31.ancree ⟨some 0, none⟩ = true := by decide
example : ProfRegPR31.ancree ⟨none, some 1⟩ = true := by decide
example : decide (RA.teneur ≠ RB.teneur) = true := by decide
example : ProfRegPR31.ancreeDuale ⟨0, ⟨some 0, none⟩⟩ ⟨1, ⟨none, some 1⟩⟩ = true := by decide

def decl : ProfRegPR37.DeclarationConcernes := ⟨1, .milieu, some 2, [3, 4], 5, some 2, .arretee, some 2030⟩
def mt : Option ProfRegPR37.MaintienMilieu := some ⟨5, 0, 1, ⟨100, 60⟩, 2030, 3⟩
def RBm : ProfRegPR37.RegistreDuMilieu Nat := ⟨decl, RB, rfl, mt⟩

-- C-07 déclaration des concernés ; C-08 maintien structuré
example : ProfRegPR37.declarationValide decl 2026 = true := by decide
example : (match mt with | some m => m.registre == decl.titulaire | none => false) = true := by decide
example : ProfRegPR37.bienForme RBm 2026 = true := by decide
example : mt.map ProfRegPR23.MaintienCONV11.solde = some 40 := by decide

-- C-04 (via PR-37) : colonne A = écart envers le titulaire
example : ProfRegPR37.ecartEnversMilieu 2026 RA 1 (some RBm) = [] := by decide
example : ProfRegPR35.ecart RB RA = [] := by decide
example : decide (ProfRegPR37.ecartEnversMilieu 2026 RA 1 (some RBm) = [] ∧ ProfRegPR37.bienForme RBm 2026 = true ∧ ProfRegPR35.ecart RB RA = []) = true := by decide

-- C-05 garde des deux silences
example : decide (ProfRegPR35.lignesVers RA RB = [] ∧ ProfRegPR35.lignesVers RB RA = []) = false := by decide

-- C-06 concordance (information)
example : decide (ProfRegPR35.Concordante RA RB) = true := by decide

-- C-10 instance de contrôle commune (CONV-16)
def ds : List ProfRegPR43.DesignationControle := [⟨0, 6, .arretee⟩, ⟨1, 6, .arretee⟩]
example : (ds.map (·.instanceCtrl)).any (ProfRegPR43.instanceCommune ds RA.teneur RB.teneur) = true := by decide

end V_ko_09_triplet_incomplet

namespace V_ko_10_instance_unilaterale

def RA : ProfRegPR35.Registre Nat := ⟨0, [⟨1, .Dplus, 100⟩]⟩
def RB : ProfRegPR35.Registre Nat := ⟨1, [⟨0, .Cplus, 100⟩]⟩

-- C-01 ancrage par côté ; C-01 et C-02 ancrage de l'écriture duale (D7)
example : ProfRegPR31.ancree ⟨some 0, none⟩ = true := by decide
example : ProfRegPR31.ancree ⟨none, some 1⟩ = true := by decide
example : decide (RA.teneur ≠ RB.teneur) = true := by decide
example : ProfRegPR31.ancreeDuale ⟨0, ⟨some 0, none⟩⟩ ⟨1, ⟨none, some 1⟩⟩ = true := by decide

def decl : ProfRegPR37.DeclarationConcernes := ⟨1, .milieu, some 2, [3, 4], 5, some 2, .arretee, some 2030⟩
def mt : Option ProfRegPR37.MaintienMilieu := some ⟨5, 0, 1, ⟨100, 60⟩, 2030, 3⟩
def RBm : ProfRegPR37.RegistreDuMilieu Nat := ⟨decl, RB, rfl, mt⟩

-- C-07 déclaration des concernés ; C-08 maintien structuré
example : ProfRegPR37.declarationValide decl 2026 = true := by decide
example : (match mt with | some m => m.registre == decl.titulaire | none => false) = true := by decide
example : ProfRegPR37.bienForme RBm 2026 = true := by decide
example : mt.map ProfRegPR23.MaintienCONV11.solde = some 40 := by decide

-- C-04 (via PR-37) : colonne A = écart envers le titulaire
example : ProfRegPR37.ecartEnversMilieu 2026 RA 1 (some RBm) = [] := by decide
example : ProfRegPR35.ecart RB RA = [] := by decide
example : decide (ProfRegPR37.ecartEnversMilieu 2026 RA 1 (some RBm) = [] ∧ ProfRegPR37.bienForme RBm 2026 = true ∧ ProfRegPR35.ecart RB RA = []) = true := by decide

-- C-05 garde des deux silences
example : decide (ProfRegPR35.lignesVers RA RB = [] ∧ ProfRegPR35.lignesVers RB RA = []) = false := by decide

-- C-06 concordance (information)
example : decide (ProfRegPR35.Concordante RA RB) = true := by decide

-- C-10 instance de contrôle commune (CONV-16)
def ds : List ProfRegPR43.DesignationControle := [⟨1, 6, .arretee⟩]
example : (ds.map (·.instanceCtrl)).any (ProfRegPR43.instanceCommune ds RA.teneur RB.teneur) = false := by decide

end V_ko_10_instance_unilaterale

namespace V_ko_11_instance_ratifiee

def RA : ProfRegPR35.Registre Nat := ⟨0, [⟨1, .Dplus, 100⟩]⟩
def RB : ProfRegPR35.Registre Nat := ⟨1, [⟨0, .Cplus, 100⟩]⟩

-- C-01 ancrage par côté ; C-01 et C-02 ancrage de l'écriture duale (D7)
example : ProfRegPR31.ancree ⟨some 0, none⟩ = true := by decide
example : ProfRegPR31.ancree ⟨none, some 1⟩ = true := by decide
example : decide (RA.teneur ≠ RB.teneur) = true := by decide
example : ProfRegPR31.ancreeDuale ⟨0, ⟨some 0, none⟩⟩ ⟨1, ⟨none, some 1⟩⟩ = true := by decide

def decl : ProfRegPR37.DeclarationConcernes := ⟨1, .milieu, some 2, [3, 4], 5, some 2, .arretee, some 2030⟩
def mt : Option ProfRegPR37.MaintienMilieu := some ⟨5, 0, 1, ⟨100, 60⟩, 2030, 3⟩
def RBm : ProfRegPR37.RegistreDuMilieu Nat := ⟨decl, RB, rfl, mt⟩

-- C-07 déclaration des concernés ; C-08 maintien structuré
example : ProfRegPR37.declarationValide decl 2026 = true := by decide
example : (match mt with | some m => m.registre == decl.titulaire | none => false) = true := by decide
example : ProfRegPR37.bienForme RBm 2026 = true := by decide
example : mt.map ProfRegPR23.MaintienCONV11.solde = some 40 := by decide

-- C-04 (via PR-37) : colonne A = écart envers le titulaire
example : ProfRegPR37.ecartEnversMilieu 2026 RA 1 (some RBm) = [] := by decide
example : ProfRegPR35.ecart RB RA = [] := by decide
example : decide (ProfRegPR37.ecartEnversMilieu 2026 RA 1 (some RBm) = [] ∧ ProfRegPR37.bienForme RBm 2026 = true ∧ ProfRegPR35.ecart RB RA = []) = true := by decide

-- C-05 garde des deux silences
example : decide (ProfRegPR35.lignesVers RA RB = [] ∧ ProfRegPR35.lignesVers RB RA = []) = false := by decide

-- C-06 concordance (information)
example : decide (ProfRegPR35.Concordante RA RB) = true := by decide

-- C-10 instance de contrôle commune (CONV-16)
def ds : List ProfRegPR43.DesignationControle := [⟨0, 6, .ratifiee⟩, ⟨1, 6, .arretee⟩]
example : (ds.map (·.instanceCtrl)).any (ProfRegPR43.instanceCommune ds RA.teneur RB.teneur) = false := by decide

end V_ko_11_instance_ratifiee

namespace V_ok_01_pret_bancaire

def RA : ProfRegPR35.Registre Nat := ⟨0, [⟨1, .Cplus, 100⟩]⟩
def RB : ProfRegPR35.Registre Nat := ⟨1, [⟨0, .Dplus, 100⟩]⟩

-- C-01 ancrage par côté ; C-01 et C-02 ancrage de l'écriture duale (D7)
example : ProfRegPR31.ancree ⟨some 0, none⟩ = true := by decide
example : ProfRegPR31.ancree ⟨some 1, none⟩ = true := by decide
example : decide (RA.teneur ≠ RB.teneur) = true := by decide
example : ProfRegPR31.ancreeDuale ⟨0, ⟨some 0, none⟩⟩ ⟨1, ⟨some 1, none⟩⟩ = true := by decide

-- C-04 état de rapprochement et écriture duale
example : ProfRegPR35.etatRapprochement RA RB = ([], []) := by decide
example : decide (ProfRegPR35.EcritureDuale RA RB) = true := by decide

-- C-05 garde des deux silences
example : decide (ProfRegPR35.lignesVers RA RB = [] ∧ ProfRegPR35.lignesVers RB RA = []) = false := by decide

-- C-06 concordance (information)
example : decide (ProfRegPR35.Concordante RA RB) = true := by decide

end V_ok_01_pret_bancaire

namespace V_ok_02_apres_remboursement

def RA : ProfRegPR35.Registre Nat := ⟨0, [⟨1, .Cplus, 100⟩, ⟨1, .Cmoins, 100⟩]⟩
def RB : ProfRegPR35.Registre Nat := ⟨1, [⟨0, .Dplus, 100⟩]⟩

-- C-01 ancrage par côté ; C-01 et C-02 ancrage de l'écriture duale (D7)
example : ProfRegPR31.ancree ⟨some 0, none⟩ = true := by decide
example : ProfRegPR31.ancree ⟨some 1, none⟩ = true := by decide
example : decide (RA.teneur ≠ RB.teneur) = true := by decide
example : ProfRegPR31.ancreeDuale ⟨0, ⟨some 0, none⟩⟩ ⟨1, ⟨some 1, none⟩⟩ = true := by decide

-- C-04 état de rapprochement et écriture duale
example : ProfRegPR35.etatRapprochement RA RB = ([⟨1, .Cmoins, 100⟩], []) := by decide
example : decide (ProfRegPR35.EcritureDuale RA RB) = false := by decide

-- C-05 garde des deux silences
example : decide (ProfRegPR35.lignesVers RA RB = [] ∧ ProfRegPR35.lignesVers RB RA = []) = false := by decide

-- C-06 concordance (information)
example : decide (ProfRegPR35.Concordante RA RB) = false := by decide

-- C-11 statut de l'écart (PR-40)
example : (ProfRegPR40.ecartQualifie .nonCommunique RA RB).map (·.2) = [.nonVerifiable] := by decide

end V_ok_02_apres_remboursement

namespace V_ok_03_riviere_arretee

def RA : ProfRegPR35.Registre Nat := ⟨0, [⟨1, .Dplus, 100⟩]⟩
def RB : ProfRegPR35.Registre Nat := ⟨1, [⟨0, .Cplus, 100⟩]⟩

-- C-01 ancrage par côté ; C-01 et C-02 ancrage de l'écriture duale (D7)
example : ProfRegPR31.ancree ⟨some 0, none⟩ = true := by decide
example : ProfRegPR31.ancree ⟨none, some 1⟩ = true := by decide
example : decide (RA.teneur ≠ RB.teneur) = true := by decide
example : ProfRegPR31.ancreeDuale ⟨0, ⟨some 0, none⟩⟩ ⟨1, ⟨none, some 1⟩⟩ = true := by decide

def decl : ProfRegPR37.DeclarationConcernes := ⟨1, .milieu, some 2, [3, 4], 5, some 2, .arretee, some 2030⟩
def mt : Option ProfRegPR37.MaintienMilieu := some ⟨5, 0, 1, ⟨100, 60⟩, 2030, 3⟩
def RBm : ProfRegPR37.RegistreDuMilieu Nat := ⟨decl, RB, rfl, mt⟩

-- C-07 déclaration des concernés ; C-08 maintien structuré
example : ProfRegPR37.declarationValide decl 2026 = true := by decide
example : (match mt with | some m => m.registre == decl.titulaire | none => false) = true := by decide
example : ProfRegPR37.bienForme RBm 2026 = true := by decide
example : mt.map ProfRegPR23.MaintienCONV11.solde = some 40 := by decide

-- C-04 (via PR-37) : colonne A = écart envers le titulaire
example : ProfRegPR37.ecartEnversMilieu 2026 RA 1 (some RBm) = [] := by decide
example : ProfRegPR35.ecart RB RA = [] := by decide
example : decide (ProfRegPR37.ecartEnversMilieu 2026 RA 1 (some RBm) = [] ∧ ProfRegPR37.bienForme RBm 2026 = true ∧ ProfRegPR35.ecart RB RA = []) = true := by decide

-- C-05 garde des deux silences
example : decide (ProfRegPR35.lignesVers RA RB = [] ∧ ProfRegPR35.lignesVers RB RA = []) = false := by decide

-- C-06 concordance (information)
example : decide (ProfRegPR35.Concordante RA RB) = true := by decide

-- C-10 instance de contrôle commune (CONV-16)
def ds : List ProfRegPR43.DesignationControle := [⟨0, 6, .arretee⟩, ⟨1, 6, .arretee⟩]
example : (ds.map (·.instanceCtrl)).any (ProfRegPR43.instanceCommune ds RA.teneur RB.teneur) = true := by decide

end V_ok_03_riviere_arretee

namespace V_ok_04_deux_silences

def RA : ProfRegPR35.Registre Nat := ⟨0, []⟩
def RB : ProfRegPR35.Registre Nat := ⟨1, []⟩

-- C-01 ancrage par côté ; C-01 et C-02 ancrage de l'écriture duale (D7)
example : ProfRegPR31.ancree ⟨some 0, none⟩ = true := by decide
example : ProfRegPR31.ancree ⟨some 1, none⟩ = true := by decide
example : decide (RA.teneur ≠ RB.teneur) = true := by decide
example : ProfRegPR31.ancreeDuale ⟨0, ⟨some 0, none⟩⟩ ⟨1, ⟨some 1, none⟩⟩ = true := by decide

-- C-04 état de rapprochement et écriture duale
example : ProfRegPR35.etatRapprochement RA RB = ([], []) := by decide
example : decide (ProfRegPR35.EcritureDuale RA RB) = true := by decide

-- C-05 garde des deux silences
example : decide (ProfRegPR35.lignesVers RA RB = [] ∧ ProfRegPR35.lignesVers RB RA = []) = true := by decide

-- C-06 concordance (information)
example : decide (ProfRegPR35.Concordante RA RB) = true := by decide

end V_ok_04_deux_silences

namespace V_ok_05_montants_differents

def RA : ProfRegPR35.Registre Nat := ⟨0, [⟨1, .Cplus, 100⟩]⟩
def RB : ProfRegPR35.Registre Nat := ⟨1, [⟨0, .Dplus, 97⟩]⟩

-- C-01 ancrage par côté ; C-01 et C-02 ancrage de l'écriture duale (D7)
example : ProfRegPR31.ancree ⟨some 0, none⟩ = true := by decide
example : ProfRegPR31.ancree ⟨some 1, none⟩ = true := by decide
example : decide (RA.teneur ≠ RB.teneur) = true := by decide
example : ProfRegPR31.ancreeDuale ⟨0, ⟨some 0, none⟩⟩ ⟨1, ⟨some 1, none⟩⟩ = true := by decide

-- C-04 état de rapprochement et écriture duale
example : ProfRegPR35.etatRapprochement RA RB = ([], []) := by decide
example : decide (ProfRegPR35.EcritureDuale RA RB) = true := by decide

-- C-05 garde des deux silences
example : decide (ProfRegPR35.lignesVers RA RB = [] ∧ ProfRegPR35.lignesVers RB RA = []) = false := by decide

-- C-06 concordance (information)
example : decide (ProfRegPR35.Concordante RA RB) = false := by decide

end V_ok_05_montants_differents
