from typing import Dict


class Product:
    """Représente un produit dans l'inventaire."""

    def __init__(self, name: str, price: float, quantity: int) -> None:
        if price < 0:
            raise ValueError("Le prix ne peut pas être négatif.")
        if quantity < 0:
            raise ValueError("La quantité ne peut pas être négative.")
        if not name.strip():
            raise ValueError("Le nom du produit ne peut pas être vide.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def restock(self, amount: int) -> None:
        """Ajoute une quantité au stock du produit."""
        if amount > 0:
            self.quantity += amount

    def sell(self, amount: int) -> bool:
        """Vend une quantité du produit, retourne True si réussi."""
        if 0 < amount <= self.quantity:
            self.quantity -= amount
            return True
        return False

    def value(self) -> float:
        """Retourne la valeur totale du stock pour ce produit."""
        return self.price * self.quantity

    def __repr__(self) -> str:
        return (
            f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"
        )


class Inventory:
    """Gère un inventaire de produits."""

    def __init__(self) -> None:
        self.products: Dict[str, Product] = {}

    def add_product(self, product: Product) -> None:
        """Ajoute un nouveau produit à l'inventaire."""
        if product.name not in self.products:
            self.products[product.name] = product

    def remove_product(self, product_name: str) -> bool:
        """Supprime un produit de l'inventaire."""
        if product_name in self.products:
            del self.products[product_name]
            return True
        return False

    def get_total_value(self) -> float:
        """Calcule la valeur totale de l'inventaire."""
        return sum(product.value() for product in self.products.values())

    def find_product(self, product_name: str) -> Product | None:
        """Recherche un produit par son nom."""
        return self.products.get(product_name)

    def __repr__(self) -> str:
        return f"Inventory(products={list(self.products.values())})"