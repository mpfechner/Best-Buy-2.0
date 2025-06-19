from promotions import Promotion


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number.")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product parameters.")

        self._name = name
        self._price = float(price)
        self._quantity = quantity
        self._active = quantity > 0

        # 👇 NEU: Promotion-Attribut (optional, kein Check)
        self._promotion = None

    def set_promotion(self, promotion):
        if not isinstance(promotion, Promotion):
            raise TypeError("Promotion must be a Promotion instance.")
        self._promotion = promotion

    def get_promotion(self):
        return self._promotion

    def get_quantity(self) -> int:
        return self._quantity

    def set_quantity(self, quantity: int) -> None:
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self._active

    def activate(self) -> None:
        self._active = True

    def deactivate(self) -> None:
        self._active = False

    def show(self) -> str:
        promo = f" (Promotion: {self._promotion})" if self._promotion else ""
        return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}{promo}"

    def buy(self, quantity: int) -> float:
        if not self._active:
            raise Exception("Product is not active.")
        if quantity > self._quantity:
            raise Exception("Not enough stock.")
        self._quantity -= quantity
        if self._quantity == 0:
            self.deactivate()

        if self._promotion:
            return self._promotion.apply_promotion(self, quantity)
        return self._price * quantity


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price, 0)

    def set_quantity(self, quantity: int) -> None:
        # Ignoriert alle Versuche, die Menge zu setzen
        pass

    def buy(self, quantity: int) -> float:
        # Darf beliebig oft gekauft werden
        return self._price * quantity

    def show(self) -> str:
        return f"{super().show()} (Non-stocked item)"


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self._maximum = maximum

    def buy(self, quantity: int) -> float:
        if quantity > self._maximum:
            raise Exception(f"Cannot buy more than {self._maximum} of this item.")
        return super().buy(quantity)

    def show(self) -> str:
        return f"{super().show()} (Limit: {self._maximum} per order)"

