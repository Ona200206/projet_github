from typing import List, Dict

class Planet:
    """Représentation d'une planète avec ses propriétés physiques et atmosphériques."""
    
    def __init__(self, name: str, mass: float, radius: float, distance_from_sun: float, atmosphere: Dict[str, float]):
        """
        Initialise une planète avec ses propriétés.
        
        :param name: Nom de la planète.
        :param mass: Masse de la planète en kilogrammes.
        :param radius: Rayon de la planète en mètres.
        :param distance_from_sun: Distance moyenne du Soleil en kilomètres.
        :param atmosphere: Composition atmosphérique (% de chaque gaz).
        """
        self.name = name
        self.mass = mass
        self.radius = radius
        self.distance_from_sun = distance_from_sun
        self.atmosphere = atmosphere

    def surface_gravity(self) -> float:
        """
        Calcule la gravité à la surface de la planète.
        
        :return: Gravité en m/s².
        """
        G = 6.67430e-11  # Constante gravitationnelle (m³/kg/s²)
        return G * self.mass / (self.radius ** 2)

    def atmosphere_summary(self) -> str:
        """
        Génère un résumé de la composition atmosphérique.
        
        :return: Chaîne décrivant les gaz principaux.
        """
        summary = ', '.join([f"{gas}: {percentage}%" for gas, percentage in self.atmosphere.items()])
        return f"Composition atmosphérique de {self.name}: {summary}"


class PlanetCatalog:
    """Catalogue pour gérer une collection de planètes."""
    
    def __init__(self):
        """Initialise un catalogue vide."""
        self.planets: List[Planet] = []

    def add_planet(self, planet: Planet) -> None:
        """
        Ajoute une planète au catalogue.
        
        :param planet: Objet Planet à ajouter.
        """
        self.planets.append(planet)

    def get_planet_by_name(self, name: str) -> Planet:
        """
        Récupère une planète par son nom.
        
        :param name: Nom de la planète.
        :return: Objet Planet correspondant.
        :raises ValueError: Si aucune planète avec ce nom n'est trouvée.
        """
        for planet in self.planets:
            if planet.name == name:
                return planet
        raise ValueError(f"Aucune planète nommée '{name}' trouvée.")

    def list_all_planets(self) -> List[str]:
        """
        Liste tous les noms des planètes dans le catalogue.
        
        :return: Liste des noms de planètes.
        """
        return [planet.name for planet in self.planets]

    def average_distance_from_sun(self) -> float:
        """
        Calcule la distance moyenne des planètes au Soleil.
        
        :return: Distance moyenne en kilomètres.
        """
        if not self.planets:
            raise ValueError("Le catalogue est vide.")
        total_distance = sum(planet.distance_from_sun for planet in self.planets)
        return total_distance / len(self.planets)
