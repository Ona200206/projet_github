from typing import List, Dict


class Planet:
    """Représentation d'une planète avec ses propriétés physiques et atmosphériques."""
    
    def __init__(self, name: str, mass: float, radius: float, distance_from_sun: float, atmosphere: Dict[str, float]):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.distance_from_sun = distance_from_sun
        self.atmosphere = atmosphere

    def surface_gravity(self) -> float:
        G = 6.67430e-11  # Constante gravitationnelle (m³/kg/s²)
        return G * self.mass / (self.radius ** 2)

    def atmosphere_summary(self) -> str:
        summary = ', '.join([f"{gas}: {percentage}%" for gas, percentage in self.atmosphere.items()])
        return f"Composition atmosphérique de {self.name}: {summary}"


class PlanetCatalog:
    """Catalogue pour gérer une collection de planètes."""
    
    def __init__(self):
        self.planets: List[Planet] = []

    def add_planet(self, planet: Planet) -> None:
        self.planets.append(planet)

    def get_planet_by_name(self, name: str) -> Planet:
        for planet in self.planets:
            if planet.name == name:
                return planet
        raise ValueError(f"Aucune planète nommée '{name}' trouvée.")

    def list_all_planets(self) -> List[str]:
        return [planet.name for planet in self.planets]

    def average_distance_from_sun(self) -> float:
        if not self.planets:
            raise ValueError("Le catalogue est vide.")
        total_distance = sum(planet.distance_from_sun for planet in self.planets)
        return total_distance / len(self.planets)


def display_menu():
    """Affiche le menu principal."""
    print("\n--- Gestion des Planètes ---")
    print("1. Ajouter une planète")
    print("2. Lister toutes les planètes")
    print("3. Afficher les détails d'une planète")
    print("4. Calculer la distance moyenne des planètes au Soleil")
    print("5. Quitter")


def main():
    catalog = PlanetCatalog()
    while True:
        display_menu()
        try:
            choice = int(input("Choisissez une option : "))
            if choice == 1:
                # Ajouter une planète
                name = input("Nom de la planète : ")
                mass = float(input("Masse (kg) : "))
                radius = float(input("Rayon (m) : "))
                distance_from_sun = float(input("Distance au Soleil (km) : "))
                atmosphere_input = input(
                    "Composition atmosphérique (exemple : Oxygène:21,Azote:78) : "
                )
                atmosphere = {k: float(v) for k, v in (item.split(":") for item in atmosphere_input.split(","))}
                planet = Planet(name, mass, radius, distance_from_sun, atmosphere)
                catalog.add_planet(planet)
                print(f"La planète '{name}' a été ajoutée avec succès.")
            elif choice == 2:
                # Lister toutes les planètes
                planets = catalog.list_all_planets()
                if not planets:
                    print("Aucune planète dans le catalogue.")
                else:
                    print("Planètes dans le catalogue :")
                    for p in planets:
                        print(f"- {p}")
            elif choice == 3:
                # Afficher les détails d'une planète
                name = input("Entrez le nom de la planète : ")
                try:
                    planet = catalog.get_planet_by_name(name)
                    print(f"--- Détails de {planet.name} ---")
                    print(f"Masse : {planet.mass} kg")
                    print(f"Rayon : {planet.radius} m")
                    print(f"Distance au Soleil : {planet.distance_from_sun} km")
                    print(f"Gravité de surface : {planet.surface_gravity():.2f} m/s²")
                    print(planet.atmosphere_summary())
                except ValueError as e:
                    print(e)
            elif choice == 4:
                # Calculer la distance moyenne au Soleil
                try:
                    avg_distance = catalog.average_distance_from_sun()
                    print(f"Distance moyenne au Soleil : {avg_distance:.2f} km")
                except ValueError as e:
                    print(e)
            elif choice == 5:
                # Quitter
                print("Au revoir !")
                break
            else:
                print("Choix invalide, veuillez réessayer.")
        except ValueError:
            print("Entrée non valide. Veuillez entrer un nombre.")
main()