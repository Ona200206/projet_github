import pytest
from bataille_navale import (
    creer_grille,
    afficher_grille,
    placer_bateaux,
    tir_valide,
    effectuer_tir,
    tous_coules,
    Grille,
)

# Test de creer_grille
def test_creer_grille() -> None:
    grille: Grille = creer_grille(5)
    assert len(grille) == 5
    assert all(len(ligne) == 5 for ligne in grille)
    assert all(cell == "~" for ligne in grille for cell in ligne)

# Test d'afficher_grille
def test_afficher_grille(capsys: pytest.CaptureFixture) -> None:
    grille: Grille = [["~", "~", "~"], ["~", "B", "~"], ["~", "~", "B"]]
    afficher_grille(grille, cacher_bateaux=False)
    captured = capsys.readouterr()
    assert "B" in captured.out

    afficher_grille(grille, cacher_bateaux=True)
    captured = capsys.readouterr()
    assert "B" not in captured.out

# Test de placer_bateaux
def test_placer_bateaux() -> None:
    grille: Grille = creer_grille(5)
    placer_bateaux(grille, 3)
    bateaux = sum(cell == "B" for ligne in grille for cell in ligne)
    assert bateaux == 3

# Test de tir_valide
def test_tir_valide() -> None:
    grille: Grille = creer_grille(5)
    assert tir_valide(0, 0, grille) is True
    assert tir_valide(-1, 0, grille) is False
    assert tir_valide(5, 5, grille) is False

# Test d'effectuer_tir
def test_effectuer_tir() -> None:
    grille_joueur: Grille = creer_grille(5)
    grille_ennemie: Grille = creer_grille(5)
    grille_ennemie[2][2] = "B"

    # Test toucher
    assert effectuer_tir(2, 2, grille_joueur, grille_ennemie) is True
    assert grille_joueur[2][2] == "X"
    assert grille_ennemie[2][2] == "X"

    # Test dans l'eau
    assert effectuer_tir(1, 1, grille_joueur, grille_ennemie) is False
    assert grille_joueur[1][1] == "O"
    assert grille_ennemie[1][1] == "O"

    # Test déjà tiré
    assert effectuer_tir(1, 1, grille_joueur, grille_ennemie) is False

# Test de tous_coules
def test_tous_coules() -> None:
    grille: Grille = [["~", "~", "~"], ["~", "B", "~"], ["~", "X", "B"]]
    assert tous_coules(grille) is False
    grille[1][1] = "X"
    grille[2][2] = "X"
    assert tous_coules(grille) is True

# Test des exceptions pour les coordonnées invalides
def test_tir_invalide() -> None:
    grille_joueur: Grille = creer_grille(5)
    grille_ennemie: Grille = creer_grille(5)
    grille_ennemie[2][2] = "B"

    # Tir hors limites
    with pytest.raises(IndexError):
        effectuer_tir(6, 6, grille_joueur, grille_ennemie)

    # Tir sur coordonnées négatives
    with pytest.raises(IndexError):
        effectuer_tir(-1, -1, grille_joueur, grille_ennemie)