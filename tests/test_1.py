import pytest
from projet_github.main import Product, Inventory

# Tests pour la classe Product
def test_product_creation():
    product = Product(name="Test", price=10.0, quantity=5)
    assert product.name == "Test"
    assert product.price == 10.0
    assert product.quantity == 5

def test_product_value():
    product = Product(name="Test", price=10.0, quantity=5)
    assert product.value() == 50.0

def test_product_invalid_creation():
    with pytest.raises(ValueError):
        Product(name="", price=10.0, quantity=5)
    with pytest.raises(ValueError):
        Product(name="Valid", price=-10.0, quantity=5)

# Tests pour la classe Inventory
def test_inventory_add_product():
    inventory = Inventory()
    product = Product(name="Test", price=10.0, quantity=5)
    inventory.add_product(product)
    assert len(inventory.products) == 1
    assert inventory.products["Test"] == product

def test_inventory_remove_product():
    inventory = Inventory()
    product = Product(name="Test", price=10.0, quantity=5)
    inventory.add_product(product)
    assert inventory.remove_product("Test") is True
    assert len(inventory.products) == 0

def test_inventory_get_total_value():
    inventory = Inventory()
    inventory.add_product(Product(name="Test1", price=10.0, quantity=5))
    inventory.add_product(Product(name="Test2", price=20.0, quantity=3))
    assert inventory.get_total_value() == 110.0

def test_inventory_find_product():
    inventory = Inventory()
    product = Product(name="Test", price=10.0, quantity=5)
    inventory.add_product(product)
    assert inventory.find_product("Test") == product
    assert inventory.find_product("Nonexistent") is None
