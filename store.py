from typing import List, Tuple
from products import Product


class Store:
    """
    Represents a store that holds and manages a collection of products.
    """

    def __init__(self, products: List[Product]):
        """
        Initializes a new store instance.

        Args:
            products (List[Product]): Initial list of products in the store.
        """
        self._products: List[Product] = products

    def add_product(self, product: Product) -> None:
        """
        Adds a product to the store.

        Args:
            product (Product): The product to add.
        """
        self._products.append(product)

    def remove_product(self, product: Product) -> None:
        """
        Removes a product from the store.

        Args:
            product (Product): The product to remove.
        """
        self._products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Calculates the total quantity of all active products in the store.

        Returns:
            int: Sum of all available product quantities.
        """
        return sum(p.quantity for p in self.get_all_products())

    def get_all_products(self) -> List[Product]:
        """
        Returns a list of all active products in the store.

        Returns:
            List[Product]: Active products only.
        """
        return [p for p in self._products if p.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Processes a customer's order.

        Args:
            shopping_list (List[Tuple[Product, int]]): A list of (product, quantity) tuples.

        Returns:
            float: Total cost of the order.

        Raises:
            Exception: If a product is inactive or lacks sufficient stock.
        """
        total = 0.0
        for product, quantity in shopping_list:
            total += product.buy(quantity)
        return total

    def __contains__(self, product: Product) -> bool:
        """
        Allows checking if a product is in the store using the 'in' operator.

        Args:
            product (Product): The product to check.

        Returns:
            bool: True if product is in store, False otherwise.
        """
        return product in self._products

    def __add__(self, other: object) -> 'Store':
        """
        Allows combining two stores using the '+' operator.

        Args:
            other (Store): Another Store instance.

        Returns:
            Store: A new Store containing products from both stores.

        Raises:
            TypeError: If other is not a Store.
        """
        if not isinstance(other, Store):
            raise TypeError("Can only add another Store.")
        return Store(self._products + other._products)
