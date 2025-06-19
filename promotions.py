from abc import ABC, abstractmethod
from products import Product


class Promotion(ABC):
    """
    Abstract base class for product promotions.
    """

    def __init__(self, name: str):
        self.name: str = name

    @abstractmethod
    def apply_promotion(self, product: Product, quantity: int) -> float:
        """
        Calculates the discounted price for a given quantity of product.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): Quantity of the product being purchased.

        Returns:
            float: Total discounted price.
        """
        pass

    def __str__(self) -> str:
        return self.name


class PercentDiscount(Promotion):
    """
    Promotion that applies a percentage discount to the total price.
    """

    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent: float = percent

    def apply_promotion(self, product: Product, quantity: int) -> float:
        original_price = product.price * quantity
        discount = original_price * (self.percent / 100)
        return original_price - discount


class SecondHalfPrice(Promotion):
    """
    Promotion where every second item is half price.
    """

    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product: Product, quantity: int) -> float:
        full_price = product.price
        pairs = quantity // 2
        remaining = quantity % 2
        total = pairs * (full_price + full_price * 0.5) + remaining * full_price
        return total


class ThirdOneFree(Promotion):
    """
    Promotion where every third item is free.
    """

    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product: Product, quantity: int) -> float:
        free_items = quantity // 3
        paid_items = quantity - free_items
        return paid_items * product.price
