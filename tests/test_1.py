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


def test_product_value_zero_quantity():
    product = Product(name="Test", price=10.0, quantity=0)
    assert product.value() == 0.0


def test_product_value_negative_price():
    with pytest.raises(ValueError):
        Product(name="Test", price=-10.0, quantity=5)


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


def test_product_invalid_creation():
    with pytest.raises(ValueError):
        Product(name="Test", price=-10.0, quantity=5)
    with pytest.raises(ValueError):
        Product(name="Test", price=10.0, quantity=-5)


def test_product_float_price():
    product = Product(name="Test", price=10.99, quantity=3)
    assert product.value() == 32.97


def test_product_sell_edge_case():
    product = Product(name="Test", price=10.0, quantity=5)
    assert not product.sell(0)  # Vendre 0
    assert not product.sell(6)  # Plus que le stock


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
    assert (
        repr(inventory)
        == "Inventory(products=[Product(name=Test, price=10.0, quantity=5)])"
    )


def test_inventory_repr_empty():
    inventory = Inventory()
    assert repr(inventory) == "Inventory(products=[])"


def test_inventory_add_product_invalid_name():
    inventory = Inventory()
    with pytest.raises(ValueError):
        inventory.add_product(Product(name="", price=10.0, quantity=5))


def test_inventory_remove_invalid_name():
    inventory = Inventory()
    assert not inventory.remove_product("")


def test_inventory_add_duplicate_names():
    inventory = Inventory()
    product1 = Product(name="Test", price=10.0, quantity=5)
    product2 = Product(name="Test", price=20.0, quantity=10)  # Même nom, différent
    inventory.add_product(product1)
    inventory.add_product(product2)
    assert inventory.products["Test"] == product1  # Pas de remplacement


def test_inventory_total_value_with_zero_price_or_quantity():
    inventory = Inventory()
    product1 = Product(name="Test1", price=0.0, quantity=5)
    product2 = Product(name="Test2", price=10.0, quantity=0)
    inventory.add_product(product1)
    inventory.add_product(product2)
    assert inventory.get_total_value() == 0.0


def test_inventory_update_existing_product():
    inventory = Inventory()
    product1 = Product(name="Test", price=10.0, quantity=5)
    product2 = Product(name="Test", price=15.0, quantity=3)  # Différente instance
    inventory.add_product(product1)
    inventory.add_product(product2)
    assert inventory.products["Test"] == product1  # Pas de mise à jour


def test_inventory_full_workflow():
    inventory = Inventory()
    product1 = Product(name="Laptop", price=1000.0, quantity=5)
    product2 = Product(name="Phone", price=800.0, quantity=10)

    inventory.add_product(product1)
    inventory.add_product(product2)

    # Vérifiez la valeur initiale
    assert inventory.get_total_value() == 13000.0

    # Vendez 3 ordinateurs portables
    assert product1.sell(3) is True
    assert product1.quantity == 2  # Vérifiez la quantité mise à jour
    assert inventory.get_total_value() == 10000.0  # Vérifiez la valeur mise à jour

    # Supprimez les téléphones
    assert inventory.remove_product("Phone") is True
    assert inventory.get_total_value() == 2000.0


def test_main_example():
    # Initialisation de l'inventaire
    inventory = Inventory()
    product1 = Product(name="Laptop", price=1200.0, quantity=5)
    product2 = Product(name="Phone", price=800.0, quantity=10)

    # Ajout des produits
    inventory.add_product(product1)
    inventory.add_product(product2)

    # Vérifiez que les produits ont été ajoutés
    assert len(inventory.products) == 2
    assert inventory.products["Laptop"] == product1
    assert inventory.products["Phone"] == product2

    # Vente de 2 ordinateurs portables
    assert product1.sell(2) is True
    assert product1.quantity == 3

    # Réapprovisionnement de 5 téléphones
    product2.restock(5)
    assert product2.quantity == 15

    # Vérifiez la valeur totale de l'inventaire
    expected_value = (3 * 1200.0) + (15 * 800.0)
    assert inventory.get_total_value() == expected_value

    # Vérifiez l'état de l'inventaire
    assert repr(inventory) == (
        "Inventory(products=[Product(name=Laptop, price=1200.0, quantity=3), "
        "Product(name=Phone, price=800.0, quantity=15)])"
    )
