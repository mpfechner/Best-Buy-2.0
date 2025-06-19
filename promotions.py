from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        pass

    def __str__(self):
        return self.name


class PercentDiscount(Promotion):
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity: int) -> float:
        return product._price * quantity * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity: int) -> float:
        full_price = product._price
        total = 0.0
        pairs = quantity // 2
        remaining = quantity % 2
        total += pairs * (full_price + full_price * 0.5)
        total += remaining * full_price
        return total


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity: int) -> float:
        free_items = quantity // 3
        paid_items = quantity - free_items
        return paid_items * product._price
