import unittest
from typing import List
from projet_github.main import (
    creer_grille,
    afficher_grille,
    placer_bateaux,
    tir_valide,
    effectuer_tir,
    tous_coules,
    Grille,
)

class TestBatailleNavale(unittest.TestCase):
    def test_creer_grille(self):
        grille = creer_grille(5)
        self.assertEqual(len(grille), 5)
        self.assertTrue(all(len(ligne) == 5 for ligne in grille))
        self.assertTrue(all(cell == "~" for ligne in grille for cell in ligne))

    def test_placer_bateaux(self):
        grille = creer_grille(5)
        placer_bateaux(grille, 3)
        bateaux = sum(cell == "B" for ligne in grille for cell in ligne)
        self.assertEqual(bateaux, 3)

    def test_tir_valide(self):
        grille = creer_grille(5)
        self.assertTrue(tir_valide(2, 2, grille))
        self.assertFalse(tir_valide(-1, 2, grille))
        self.assertFalse(tir_valide(2, 5, grille))

    def test_effectuer_tir(self):
        grille_joueur = creer_grille(5)
        grille_ennemie = creer_grille(5)
        grille_ennemie[2][2] = "B"
        self.assertTrue(effectuer_tir(2, 2, grille_joueur, grille_ennemie))
        self.assertEqual(grille_joueur[2][2], "X")
        self.assertEqual(grille_ennemie[2][2], "X")

        self.assertFalse(effectuer_tir(3, 3, grille_joueur, grille_ennemie))
        self.assertEqual(grille_joueur[3][3], "O")
        self.assertEqual(grille_ennemie[3][3], "O")

        self.assertFalse(effectuer_tir(2, 2, grille_joueur, grille_ennemie))  # Déjà tiré
        self.assertEqual(grille_joueur[2][2], "X")

    def test_tous_coules(self):
        grille = creer_grille(5)
        self.assertTrue(tous_coules(grille))  # Aucune case "B"

        grille[1][1] = "B"
        self.assertFalse(tous_coules(grille))

        grille[1][1] = "X"
        self.assertTrue(tous_coules(grille))

    def test_afficher_grille(self):
        # Test basique pour s'assurer que la fonction ne génère pas d'erreur
        grille = creer_grille(3)
        try:
            afficher_grille(grille)  # Sortie visuelle, pas de vérification ici
            afficher_grille(grille, cacher_bateaux=True)
        except Exception as e:
            self.fail(f"afficher_grille a levé une exception : {e}")

if __name__ == "_main_":
   unittest.main()