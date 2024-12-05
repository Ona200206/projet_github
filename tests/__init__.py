import pytest
from planet_management import Planet, PlanetCatalog

def test_planet_creation():
    planet = Planet("Terre", 5.972e24, 6371000, 149.6e6, {"Azote": 78, "Oxygène": 21, "Argon": 1})
    assert planet.name == "Terre"
    assert round(planet.surface_gravity(), 2) == 9.81
    assert "Azote: 78%" in planet.atmosphere_summary()

def test_catalog_operations():
    catalog = PlanetCatalog()
    earth = Planet("Terre", 5.972e24, 6371000, 149.6e6, {"Azote": 78, "Oxygène": 21, "Argon": 1})
    mars = Planet("Mars", 6.39e23, 3389500, 227.9e6, {"CO2": 95.32, "Azote": 2.7, "Argon": 1.6})
    
    catalog.add_planet(earth)
    catalog.add_planet(mars)
    
    assert catalog.list_all_planets() == ["Terre", "Mars"]
    assert catalog.get_planet_by_name("Mars").name == "Mars"
    assert round(catalog.average_distance_from_sun(), 1) == 188.75e6

def test_invalid_operations():
    catalog = PlanetCatalog()
    with pytest.raises(ValueError, match="Aucune planète nommée 'Jupiter' trouvée."):
        catalog.get_planet_by_name("Jupiter")
    
    with pytest.raises(ValueError, match="Le catalogue est vide."):
        catalog.average_distance_from_sun()
