import pytest
from products import Product

def test_create_valid_product():
    p = Product("Test", 99.99, 10)
    assert p.quantity == 10
    assert p.is_active() is True

def test_create_invalid_product():
    with pytest.raises(ValueError):
        Product("", 99.99, 10)
    with pytest.raises(ValueError):
        Product("Test", -5, 10)
    with pytest.raises(ValueError):
        Product("Test", 99.99, -3)

def test_product_becomes_inactive_when_quantity_zero():
    p = Product("Test", 50, 1)
    p.buy(1)
    assert p.quantity == 0
    assert p.is_active() is False

def test_buy_reduces_quantity_and_returns_total_price():
    p = Product("Test", 20, 5)
    price = p.buy(3)
    assert price == 60
    assert p.quantity == 2

def test_buy_more_than_stock_raises_exception():
    p = Product("Test", 30, 2)
    with pytest.raises(Exception, match="Not enough stock."):
        p.buy(5)

def test_buy_inactive_product_raises_exception():
    p = Product("Test", 20, 1)
    p.buy(1)
    with pytest.raises(Exception, match="Product is not active."):
        p.buy(1)
