
from projet_github.main import Product, Inventory


def test_product_creation():
    product = Product(name="Test", price=10.0, quantity=5)
    assert product.name == "Test"
    assert product.price == 10.0
    assert product.quantity == 5


def test_product_value():
    product = Product(name="Test", price=10.0, quantity=5)
    assert product.value() == 50.0


def test_product_sell():
    product = Product(name="Test", price=10.0, quantity=5)
    assert product.sell(3) is True
    assert product.quantity == 2
    assert not product.sell(3)  # Plus lisible


def test_product_restock():
    product = Product(name="Test", price=10.0, quantity=5)
    product.restock(5)
    assert product.quantity == 10


def test_inventory_add_remove():
    inventory = Inventory()
    product = Product(name="Test", price=10.0, quantity=5)

    inventory.add_product(product)
    assert len(inventory.products) == 1

    inventory.remove_product("Test")
    assert len(inventory.products) == 0


def test_inventory_value():
    inventory = Inventory()
    product1 = Product(name="Laptop", price=1000.0, quantity=3)
    product2 = Product(name="Phone", price=500.0, quantity=5)

    inventory.add_product(product1)
    inventory.add_product(product2)

    assert inventory.get_total_value() == 5500.0


def test_find_product():
    inventory = Inventory()
    product = Product(name="Test", price=10.0, quantity=5)

    inventory.add_product(product)
    found_product = inventory.find_product("Test")

    assert found_product is not None
    assert found_product.name == "Test"
    assert found_product.price == 10.0
    assert found_product.quantity == 5