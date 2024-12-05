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
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"


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


def run_inventory_interface():
    """Interface utilisateur textuelle pour gérer l'inventaire."""
    inventory = Inventory()

    while True:
        print("\n--- Gestion de l'inventaire ---")
        print("1. Ajouter un produit")
        print("2. Supprimer un produit")
        print("3. Vendre un produit")
        print("4. Réapprovisionner un produit")
        print("5. Afficher la valeur totale de l'inventaire")
        print("6. Afficher les produits")
        print("7. Quitter")

        try:
            choice = int(input("Choisissez une option: "))
        except ValueError:
            print("Choix invalide. Veuillez entrer un nombre.")
            continue

        if choice == 1:
            name = input("Nom du produit: ").strip()
            try:
                price = float(input("Prix du produit: "))
                quantity = int(input("Quantité: "))
                inventory.add_product(Product(name, price, quantity))
                print(f"Produit {name} ajouté.")
            except ValueError as e:
                print(f"Erreur: {e}")
        elif choice == 2:
            name = input("Nom du produit à supprimer: ").strip()
            if inventory.remove_product(name):
                print(f"Produit {name} supprimé.")
            else:
                print(f"Produit {name} introuvable.")
        elif choice == "3":
            name = input("Nom du produit à vendre : ")
            quantity = int(input("Quantité à vendre : "))
            product = inventory.find_product(name)
            if product:
                if product.sell(quantity):
                    print(f"{quantity} unités de {name} vendues.")
                else:
                    print("Stock insuffisant pour la vente.")  # Correction ici
            else:
                print("Produit introuvable.")
        elif choice == "4":
            name = input("Nom du produit à réapprovisionner : ")
            quantity = int(input("Quantité à ajouter : "))
            product = inventory.find_product(name)
            if product:
                if quantity > 0:
                    product.restock(quantity)
                    print(f"Produit {name} réapprovisionné.")
                else:
                    print("Quantité invalide pour le réapprovisionnement.")  # Correction ici
            else:
                print("Produit introuvable.")
        elif choice == 5:
            print(f"Valeur totale de l'inventaire: {inventory.get_total_value():.2f}")
        elif choice == 6:
            print("Produits dans l'inventaire:")
            print(inventory)
        elif choice == "7":
            print("Quitter le programme.")  # Correction ici
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    run_inventory_interface()
