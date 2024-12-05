import random
from typing import List, Tuple

# Constantes
TAILLE_GRILLE: int = 5
NB_BATEAUX: int = 3
Grille = List[List[str]]

def creer_grille(taille: int) -> Grille:
    """Crée une grille vide de taille donnée."""
    return [["~"] * taille for _ in range(taille)]

def afficher_grille(grille: Grille, cacher_bateaux: bool = False) -> None:
    """Affiche la grille dans un format lisible."""
    print("  " + " ".join(map(str, range(len(grille)))))
    for i, ligne in enumerate(grille):
        ligne_affichee = [case if not cacher_bateaux or case != "B" else "~" for case in ligne]
        print(f"{i} " + " ".join(ligne_affichee))

def placer_bateaux(grille: Grille, nb_bateaux: int) -> None:
    """Place un nombre donné de bateaux sur la grille aléatoirement."""
    bateaux_places = 0
    while bateaux_places < nb_bateaux:
        x, y = random.randint(0, TAILLE_GRILLE - 1), random.randint(0, TAILLE_GRILLE - 1)
        if grille[x][y] == "~":
            grille[x][y] = "B"
            bateaux_places += 1

def tir_valide(x: int, y: int, grille: Grille) -> bool:
    """Vérifie si les coordonnées du tir sont valides."""
    return 0 <= x < len(grille) and 0 <= y < len(grille[0])

def effectuer_tir(x: int, y: int, grille_joueur: Grille, grille_ennemie: Grille) -> bool:
    """Gère un tir sur la grille ennemie."""
    if grille_ennemie[x][y] == "B":
        print("Touché !")
        grille_joueur[x][y] = "X"
        grille_ennemie[x][y] = "X"
        return True
    elif grille_ennemie[x][y] == "~":
        print("Dans l'eau...")
        grille_joueur[x][y] = "O"
        grille_ennemie[x][y] = "O"
        return False
    else:
        print("Déjà tiré ici !")
        return False

def tous_coules(grille: Grille) -> bool:
    """Vérifie si tous les bateaux de la grille sont coulés."""
    return all(case != "B" for ligne in grille for case in ligne)

def lire_coordonnees() -> Tuple[int, int]:
    """Lit et valide les coordonnées entrées par l'utilisateur."""
    while True:
        try:
            x, y = map(int, input("Entrez les coordonnées (format: x y) : ").split())
            return x, y
        except ValueError:
            print("Entrée invalide. Utilisez le format : x y")

def bataille_navale() -> None:
    """Lance le jeu de bataille navale."""
    print("Bienvenue dans la bataille navale simplifiée !")
    grille_joueur: Grille = creer_grille(TAILLE_GRILLE)
    grille_ennemie: Grille = creer_grille(TAILLE_GRILLE)
    placer_bateaux(grille_ennemie, NB_BATEAUX)
    tours: int = 0

    while not tous_coules(grille_ennemie):
        print("\nVotre grille :")
        afficher_grille(grille_joueur)
        x, y = lire_coordonnees()
        if tir_valide(x, y, grille_joueur):
            effectuer_tir(x, y, grille_joueur, grille_ennemie)
            tours += 1
        else:
            print("Coordonnées invalides. Réessayez.")

    print("\nFélicitations, vous avez coulé tous les bateaux ennemis !")
    print(f"Vous avez gagné en {tours} tours.")
    afficher_grille(grille_ennemie)

# Point d'entrée
if __name__ == "_main_":
    bataille_navale()