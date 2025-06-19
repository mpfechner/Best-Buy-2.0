class Product:
    """
    Represents a product available in the store.

    Attributes:
        _name (str): The name of the product.
        _price (float): The price of a single unit.
        _quantity (int): The number of items in stock.
        _active (bool): Whether the product is available for purchase.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a new product instance.

        Args:
            name (str): Product name.
            price (float): Price per unit (must be non-negative).
            quantity (int): Number of items in stock (must be non-negative).

        Raises:
            TypeError: If any argument has the wrong type.
            ValueError: If name is empty or price/quantity is negative.
        """
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
        self._active = quantity > 0  # Active only if quantity is not zero

    def get_quantity(self) -> int:
        """
        Returns the current quantity of the product.

        Returns:
            int: Available stock.
        """
        return self._quantity

    def set_quantity(self, quantity: int) -> None:
        """
        Sets the available quantity. Deactivates the product if quantity is zero.

        Args:
            quantity (int): New quantity (must be non-negative).

        Raises:
            ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Checks whether the product is active.

        Returns:
            bool: True if active, False otherwise.
        """
        return self._active

    def activate(self) -> None:
        """Activates the product."""
        self._active = True

    def deactivate(self) -> None:
        """Deactivates the product."""
        self._active = False

    def show(self) -> str:
        """
        Returns a string representation of the product.

        Returns:
            str: Product details in readable format.
        """
        return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}"

    def buy(self, quantity: int) -> float:
        """
        Processes a purchase and updates the quantity.

        Args:
            quantity (int): Amount to purchase.

        Returns:
            float: Total price of the purchase.

        Raises:
            Exception: If the product is inactive or not enough stock.
        """
        if not self._active:
            raise Exception("Product is not active.")
        if quantity > self._quantity:
            raise Exception("Not enough stock.")
        self._quantity -= quantity
        if self._quantity == 0:
            self.deactivate()
        return self._price * quantity
