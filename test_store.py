import pytest
from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree
from store import Store


def test_product_buy_without_promotion():
    p = Product("Test", 100, 5)
    assert p.buy(2) == 200
    assert p.quantity == 3


def test_product_buy_with_percent_discount():
    p = Product("Test", 100, 5)
    promo = PercentDiscount("30% off", 30)
    p.set_promotion(promo)
    assert p.buy(2) == 140


def test_product_buy_with_second_half_price():
    p = Product("Test", 100, 10)
    p.set_promotion(SecondHalfPrice("2nd Half"))
    assert p.buy(3) == 250  # 100 + 50 + 100


def test_product_buy_with_third_one_free():
    p = Product("Test", 100, 6)
    p.set_promotion(ThirdOneFree("Buy 2 Get 1"))
    assert p.buy(3) == 200  # 2 zahlen, 1 gratis


def test_nonstocked_product():
    p = NonStockedProduct("License", 50)
    assert p.quantity == 0
    assert p.buy(10) == 500  # keine Lagergrenze


def test_limited_product_allows_valid_quantity():
    p = LimitedProduct("Shipping", 10, 100, maximum=1)
    assert p.buy(1) == 10


def test_limited_product_blocks_invalid_quantity():
    p = LimitedProduct("Shipping", 10, 100, maximum=1)
    with pytest.raises(Exception):
        p.buy(2)


def test_store_order_successful():
    p1 = Product("Item1", 50, 5)
    p2 = Product("Item2", 30, 5)
    store = Store([p1, p2])
    shopping = [(p1, 2), (p2, 1)]
    assert store.order(shopping) == 130
    assert p1.quantity == 3
    assert p2.quantity == 4


def test_store_order_exceeds_quantity():
    p = Product("Limited", 100, 1)
    store = Store([p])
    with pytest.raises(Exception):
        store.order([(p, 2)])


def test_product_comparison():
    mac = Product("Mac", 1200, 1)
    pixel = Product("Pixel", 500, 1)
    assert mac > pixel
    assert pixel < mac


def test_store_contains_and_add():
    p1 = Product("A", 10, 1)
    p2 = Product("B", 20, 1)
    s1 = Store([p1])
    s2 = Store([p2])
    s3 = s1 + s2
    assert p1 in s3
    assert p2 in s3
