from promotions import Promotion


class Product:
    """
    Represents a generic product in the store.
    """

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        self._active = quantity > 0
        self._promotion = None

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number.")
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = float(value)

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Quantity must be an integer.")
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = value
        if value == 0:
            self.deactivate()
        else:
            self.activate()

    def is_active(self) -> bool:
        return self._active

    def activate(self) -> None:
        self._active = True

    def deactivate(self) -> None:
        self._active = False

    def set_promotion(self, promotion: Promotion) -> None:
        if not isinstance(promotion, Promotion):
            raise TypeError("Promotion must be a Promotion instance.")
        self._promotion = promotion

    def get_promotion(self) -> Promotion:
        return self._promotion

    def buy(self, quantity: int) -> float:
        if not self._active:
            raise Exception("Product is not active.")
        if quantity > self.quantity:
            raise Exception("Not enough stock.")
        self.quantity -= quantity
        if self._promotion:
            return self._promotion.apply_promotion(self, quantity)
        return self.price * quantity

    def __str__(self) -> str:
        promo = f" (Promotion: {self._promotion})" if self._promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promo}"

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self.price > other.price


class NonStockedProduct(Product):
    """
    A product that has unlimited quantity (e.g. digital goods).
    """

    def __init__(self, name: str, price: float):
        super().__init__(name, price, 0)

    def set_quantity(self, quantity: int) -> None:
        pass  # Quantity is always 0

    def buy(self, quantity: int) -> float:
        return self.price * quantity

    def __str__(self) -> str:
        return f"{super().__str__()} (Non-stocked item)"


class LimitedProduct(Product):
    """
    A product that can only be bought in limited quantity per order.
    """

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self._maximum = maximum

    def buy(self, quantity: int) -> float:
        if quantity > self._maximum:
            raise Exception(f"Cannot buy more than {self._maximum} of this item.")
        return super().buy(quantity)

    def __str__(self) -> str:
        return f"{super().__str__()} (Limit: {self._maximum} per order)"
