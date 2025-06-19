from typing import List, Tuple
from products import Product


class Store:
    """
    Represents a store containing a collection of products.

    Attributes:
        _products (List[Product]): The list of products in the store.
    """

    def __init__(self, products: List[Product]):
        """
        Initializes a new store instance.

        Args:
            products (List[Product]): Initial list of products in the store.
        """
        self._products = products

    def add_product(self, product: Product) -> None:
        """
        Adds a new product to the store.

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
        Calculates the total quantity of all products in the store.

        Returns:
            int: Sum of all available product quantities.
        """
        return sum(p.get_quantity() for p in self._products)

    def get_all_products(self) -> List[Product]:
        """
        Returns a list of all active products in the store.

        Returns:
            List[Product]: Active products only.
        """
        return [p for p in self._products if p.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Processes a multi-product order.

        Args:
            shopping_list (List[Tuple[Product, int]]): A list of (product, quantity) pairs.

        Returns:
            float: Total price of the order.

        Raises:
            Exception: If a product is inactive or quantity is unavailable.
        """
        # pylint: disable=R0201
        total = 0.0
        for product, quantity in shopping_list:
            total += product.buy(quantity)
        return total
