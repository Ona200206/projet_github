import pytest
from projet_github.main import Planet, PlanetCatalog


def test_planet_creation():
    """Test de la création d'une planète et de ses propriétés."""
    planet = Planet("Terre", 5.972e24, 6371000, 149.6e6, {"Azote": 78, "Oxygène": 21, "Argon": 1})
    assert planet.name == "Terre"
    assert round(planet.surface_gravity(), 2) == 9.81
    assert "Azote: 78%" in planet.atmosphere_summary()


def test_catalog_operations():
    """Test des opérations sur le catalogue."""
    catalog = PlanetCatalog()
    earth = Planet("Terre", 5.972e24, 6371000, 149.6e6, {"Azote": 78, "Oxygène": 21, "Argon": 1})
    mars = Planet("Mars", 6.39e23, 3389500, 227.9e6, {"CO2": 95.32, "Azote": 2.7, "Argon": 1.6})

    # Ajouter des planètes
    catalog.add_planet(earth)
    catalog.add_planet(mars)

    # Lister les planètes
    assert catalog.list_all_planets() == ["Terre", "Mars"]

    # Récupérer une planète par nom
    assert catalog.get_planet_by_name("Mars").name == "Mars"

    # Distance moyenne des planètes
    assert round(catalog.average_distance_from_sun(), 1) == 188.75e6


def test_invalid_operations():
    """Test des comportements en cas d'opérations invalides."""
    catalog = PlanetCatalog()

    # Chercher une planète qui n'existe pas
    with pytest.raises(ValueError, match="Aucune planète nommée 'Jupiter' trouvée."):
        catalog.get_planet_by_name("Jupiter")

    # Calculer la distance moyenne dans un catalogue vide
    with pytest.raises(ValueError, match="Le catalogue est vide."):
        catalog.average_distance_from_sun()


def test_planet_atmosphere_parsing():
    """Test de la gestion des données atmosphériques."""
    atmosphere_input = "Azote:78,Oxygène:21,Argon:1"
    atmosphere = {k: float(v) for k, v in (item.split(":") for item in atmosphere_input.split(","))}
    assert atmosphere == {"Azote": 78.0, "Oxygène": 21.0, "Argon": 1.0}


def test_catalog_integration():
    """Test d'intégration sur les fonctionnalités combinées."""
    catalog = PlanetCatalog()

    # Ajouter plusieurs planètes
    planet_data = [
        ("Mercure", 3.301e23, 2439700, 57.9e6, {"Hélium": 42, "Hydrogène": 56}),
        ("Venus", 4.867e24, 6051800, 108.2e6, {"CO2": 96.5, "Azote": 3.5}),
        ("Terre", 5.972e24, 6371000, 149.6e6, {"Azote": 78, "Oxygène": 21, "Argon": 1}),
    ]

    for name, mass, radius, distance, atmosphere in planet_data:
        catalog.add_planet(Planet(name, mass, radius, distance, atmosphere))

    # Vérifier les ajouts
    assert len(catalog.planets) == 3
    assert catalog.list_all_planets() == ["Mercure", "Venus", "Terre"]

    # Vérifier les détails d'une planète
    earth = catalog.get_planet_by_name("Terre")
    assert earth.name == "Terre"
    assert round(earth.surface_gravity(), 2) == 9.81
    assert "Oxygène: 21%" in earth.atmosphere_summary()
