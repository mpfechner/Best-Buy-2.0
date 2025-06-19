from typing import List
from products import Product
from store import Store


def start(store: Store) -> None:
    """
    Launches the interactive store menu.

    Args:
        store (Store): The store instance to operate on.
    """
    while True:
        print_menu()
        choice = input("Please choose a number: ").strip()

        if choice == "1":
            list_products(store)
        elif choice == "2":
            show_total_quantity(store)
        elif choice == "3":
            make_order(store)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def print_menu() -> None:
    """Displays the main store menu."""
    print("   Store Menu")
    print("   ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def list_products(store: Store) -> None:
    """
    Lists all active products in the store.

    Args:
        store (Store): The store to list products from.
    """
    print("\nAvailable products:")
    for product in store.get_all_products():
        print(product.show())


def show_total_quantity(store: Store) -> None:
    """
    Displays the total quantity of all products in the store.

    Args:
        store (Store): The store to calculate quantities from.
    """
    total = store.get_total_quantity()
    print(f"\nTotal quantity in store: {total}")


def make_order(store: Store) -> None:
    """
    Handles the order process by prompting the user to select products and quantities.

    Args:
        store (Store): The store to order from.
    """
    shopping_list: List[tuple[Product, int]] = []
    products = store.get_all_products()

    print("\nEnter the number of the product and quantity to order.")
    for i, product in enumerate(products):
        print(f"{i + 1}. {product.show()}")

    while True:
        try:
            prod_input = input("Product number (or press Enter to finish): ").strip()
            if not prod_input:
                break
            index = int(prod_input) - 1
            if index < 0 or index >= len(products):
                print("Invalid product number.")
                continue
            quantity = int(input("Quantity: "))
            shopping_list.append((products[index], quantity))
        except ValueError as input_error:
            print(f"Invalid input: {input_error}")

    try:
        total_price = store.order(shopping_list)
        print(f"\nOrder placed. Total cost: {total_price} dollars.")
    except Exception as order_error:  # noqa: W0703
        print(f"Error placing order: {order_error}")


def main() -> None:
    """Creates a sample store and starts the interactive CLI."""
    product_list = [
        Product("MacBook Air M2", 1450, 100),
        Product("Bose QuietComfort Earbuds", 250, 500),
        Product("Google Pixel 7", 500, 250),
    ]
    store = Store(product_list)
    start(store)


if __name__ == "__main__":
    main()
