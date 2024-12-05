
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


def test_product_value_zero_quantity():
    product = Product(name="Test", price=10.0, quantity=0)
    assert product.value() == 0.0


def test_product_value_negative_price():
    product = Product(name="Test", price=-10.0, quantity=5)
    assert product.value() == -50.0


def test_product_sell_success():
    product = Product(name="Test", price=10.0, quantity=5)
    assert product.sell(3) is True
    assert product.quantity == 2


def test_product_sell_failure():
    product = Product(name="Test", price=10.0, quantity=5)
    assert not product.sell(6)  # Trop à vendre
    assert not product.sell(-1)  # Quantité invalide
    assert not product.sell(0)  # Quantité invalide


def test_product_sell_boundary():
    product = Product(name="Test", price=10.0, quantity=1)
    assert product.sell(1) is True
    assert product.quantity == 0


def test_product_restock_success():
    product = Product(name="Test", price=10.0, quantity=5)
    product.restock(5)
    assert product.quantity == 10


def test_product_restock_failure():
    product = Product(name="Test", price=10.0, quantity=5)
    product.restock(-5)  # Quantité invalide
    assert product.quantity == 5  # Quantité inchangée


def test_product_repr():
    product = Product(name="Test", price=10.0, quantity=5)
    assert repr(product) == "Product(name=Test, price=10.0, quantity=5)"


# Tests pour la classe Inventory
def test_inventory_creation():
    inventory = Inventory()
    assert len(inventory.products) == 0


def test_inventory_add_product():
    inventory = Inventory()
    product = Product(name="Test", price=10.0, quantity=5)
    inventory.add_product(product)
    assert len(inventory.products) == 1
    assert inventory.products["Test"] == product


def test_inventory_add_multiple_products():
    inventory = Inventory()
    product1 = Product(name="Test", price=10.0, quantity=5)
    product2 = Product(name="Test2", price=20.0, quantity=3)
    inventory.add_product(product1)
    inventory.add_product(product2)
    assert len(inventory.products) == 2


def test_inventory_add_existing_product():
    inventory = Inventory()
    product = Product(name="Test", price=10.0, quantity=5)
    inventory.add_product(product)
    inventory.add_product(product)  # Réajout du même produit
    assert len(inventory.products) == 1  # Pas de duplication


def test_inventory_remove_product_success():
    inventory = Inventory()
    product = Product(name="Test", price=10.0, quantity=5)
    inventory.add_product(product)
    assert inventory.remove_product("Test") is True
    assert len(inventory.products) == 0


def test_inventory_remove_product_failure():
    inventory = Inventory()
    assert not inventory.remove_product("NonExistent")


def test_inventory_get_total_value():
    inventory = Inventory()
    product1 = Product(name="Laptop", price=1000.0, quantity=3)
    product2 = Product(name="Phone", price=500.0, quantity=5)
    inventory.add_product(product1)
    inventory.add_product(product2)
    assert inventory.get_total_value() == 5500.0


def test_inventory_get_total_value_empty():
    inventory = Inventory()
    assert inventory.get_total_value() == 0.0


def test_inventory_find_product_success():
    inventory = Inventory()
    product = Product(name="Test", price=10.0, quantity=5)
    inventory.add_product(product)
    found_product = inventory.find_product("Test")
    assert found_product == product


def test_inventory_find_product_failure():
    inventory = Inventory()
    assert inventory.find_product("NonExistent") is None


def test_inventory_find_product_similar_name():
    inventory = Inventory()
    product = Product(name="Test", price=10.0, quantity=5)
    inventory.add_product(product)
    assert inventory.find_product("Test2") is None


def test_inventory_repr():
    inventory = Inventory()
    product = Product(name="Test", price=10.0, quantity=5)
    inventory.add_product(product)
    assert repr(inventory) == "Inventory(products=[Product(name=Test, price=10.0, quantity=5)])"


def test_inventory_repr_empty():
    inventory = Inventory()
    assert repr(inventory) == "Inventory(products=[])"
