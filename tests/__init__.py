import pytest
from typing import List
from projet_github.main import (
    creer_grille,
    afficher_grille,
    placer_bateaux,
    tir_valide,
    effectuer_tir,
    tous_coules,
    TAILLE_GRILLE,
    NB_BATEAUX,
    bataille_navale,
)

import io
import sys

Grille = List[List[str]]

# Fixtures
@pytest.fixture
def grille_vide() -> Grille:
    """Fixture pour une grille vide."""
    return creer_grille(TAILLE_GRILLE)

@pytest.fixture
def grille_avec_bateaux() -> Grille:
    """Fixture pour une grille avec des bateaux placés."""
    grille = creer_grille(TAILLE_GRILLE)
    placer_bateaux(grille, NB_BATEAUX)
    return grille

# Tests pour les fonctions principales
def test_creer_grille() -> None:
    """Teste la création d'une grille vide."""
    grille = creer_grille(3)
    assert len(grille) == 3
    assert all(len(ligne) == 3 for ligne in grille)
    assert all(cell == "~" for ligne in grille for cell in ligne)

def test_placer_bateaux(grille_vide: Grille) -> None:
    """Teste le placement de bateaux."""
    placer_bateaux(grille_vide, NB_BATEAUX)
    bateaux = sum(cell == "B" for ligne in grille_vide for cell in ligne)
    assert bateaux == NB_BATEAUX

def test_tir_valide(grille_vide: Grille) -> None:
    """Teste la validation des tirs."""
    assert tir_valide(0, 0, grille_vide) is True
    assert tir_valide(TAILLE_GRILLE, 0, grille_vide) is False
    assert tir_valide(0, TAILLE_GRILLE, grille_vide) is False
    assert tir_valide(-1, 0, grille_vide) is False

def test_effectuer_tir_touché(grille_vide: Grille) -> None:
    """Teste un tir qui touche un bateau."""
    grille_vide[1][1] = "B"
    joueur_grille = creer_grille(TAILLE_GRILLE)
    assert effectuer_tir(1, 1, joueur_grille, grille_vide) is True
    assert joueur_grille[1][1] == "X"
    assert grille_vide[1][1] == "X"

def test_effectuer_tir_raté(grille_vide: Grille) -> None:
    """Teste un tir qui rate."""
    joueur_grille = creer_grille(TAILLE_GRILLE)
    assert effectuer_tir(0, 0, joueur_grille, grille_vide) is False
    assert joueur_grille[0][0] == "O"
    assert grille_vide[0][0] == "O"

def test_effectuer_tir_déjà_tiré(grille_vide: Grille) -> None:
    """Teste un tir sur une case déjà touchée."""
    joueur_grille = creer_grille(TAILLE_GRILLE)
    grille_vide[0][0] = "O"
    joueur_grille[0][0] = "O"
    assert effectuer_tir(0, 0, joueur_grille, grille_vide) is False

def test_tous_coules(grille_vide: Grille, grille_avec_bateaux: Grille) -> None:
    """Teste si tous les bateaux sont coulés."""
    assert tous_coules(grille_vide) is True
    assert tous_coules(grille_avec_bateaux) is False

    # Couler tous les bateaux
    for x in range(TAILLE_GRILLE):
        for y in range(TAILLE_GRILLE):
            if grille_avec_bateaux[x][y] == "B":
                grille_avec_bateaux[x][y] = "X"

    assert tous_coules(grille_avec_bateaux) is True

# Tests supplémentaires pour augmenter la couverture
def test_afficher_grille(grille_vide: Grille) -> None:
    """Teste l'affichage d'une grille."""
    captured_output = io.StringIO()
    sys.stdout = captured_output
    afficher_grille(grille_vide)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert "0 1 2 3 4" in output  # Vérifie les indices
    assert all("~" in ligne for ligne in output.split("\n"))  # Vérifie les symboles de grille vide

def test_tir_valide_extremes(grille_vide: Grille) -> None:
    """Teste les coordonnées extrêmes pour tir_valide."""
    assert tir_valide(-1, 0, grille_vide) is False
    assert tir_valide(0, -1, grille_vide) is False
    assert tir_valide(TAILLE_GRILLE, 0, grille_vide) is False
    assert tir_valide(0, TAILLE_GRILLE, grille_vide) is False

def test_effectuer_tir_sur_grille_pleine(grille_vide: Grille) -> None:
    """Teste le tir sur une grille pleine."""
    for x in range(TAILLE_GRILLE):
        for y in range(TAILLE_GRILLE):
            grille_vide[x][y] = "B"
    joueur_grille = creer_grille(TAILLE_GRILLE)
    assert effectuer_tir(0, 0, joueur_grille, grille_vide) is True
    assert joueur_grille[0][0] == "X"
    assert grille_vide[0][0] == "X"

def test_tous_coules_cases_speciales() -> None:
    """Teste tous_coules avec des grilles spéciales."""
    grille_pleine = [["B"] * TAILLE_GRILLE for _ in range(TAILLE_GRILLE)]
    assert tous_coules(grille_pleine) is False  # Tous les bateaux présents

    grille_vide = [["~"] * TAILLE_GRILLE for _ in range(TAILLE_GRILLE)]
    assert tous_coules(grille_vide) is True  # Aucun bateau présent

    grille_mixte = [["B", "X", "~", "O", "B"] for _ in range(TAILLE_GRILLE)]
    assert tous_coules(grille_mixte) is False  # Bateaux encore présents

def test_bataille_navale_simulation(monkeypatch) -> None:
    """Simule une partie de bataille navale."""
    inputs = iter(["0 0", "1 1", "2 2", "3 3", "4 4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    captured_output = io.StringIO()
    sys.stdout = captured_output
    bataille_navale()
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert "Félicitations" in output
    assert "Touché" in output or "Dans l'eau" in output
