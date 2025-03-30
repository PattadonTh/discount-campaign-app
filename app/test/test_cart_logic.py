from core.item import Item
from core.cart import Cart
from core.discount import (
    FixedDiscount,
    PercentageDiscount,
    CategoryPercentageDiscount,
    PointDiscount,
    SpecialDiscount,
)


def test_fixed_discount():
    items = [Item("T-Shirt", 350, "Clothing"), Item("Hat", 250, "Accessories")]
    cart = Cart(items)
    discount = FixedDiscount(50)
    print("Before applying discount, total is:", cart.total)
    cart.apply_discount([discount])
    print("Cart total after FixedDiscount:", cart.total)
    assert cart.total == 550


def test_percentage_discount():
    items = [Item("T-Shirt", 350, "Clothing"), Item("Hat", 250, "Accessories")]
    cart = Cart(items)
    discount = PercentageDiscount(10)
    print("Before applying discount, total is:", cart.total)
    cart.apply_discount([discount])
    print("Cart total after PercentageDiscount:", cart.total)
    assert cart.total == 540


def test_category_percentage_discount():
    items = [Item("T-Shirt", 350, "Clothing"), Item("Hoodies", 700, "Clothing"), Item("Watch", 850, "Accessories"), Item("Bag", 640, "Accessories")]
    category_discounts = {"Clothing": 15}
    cart = Cart(items)
    discount = CategoryPercentageDiscount(category_discounts)
    print("Before applying discount, total is:", cart.total)
    cart.apply_discount([discount])
    print("Cart total after CategoryPercentageDiscount:", cart.total)
    assert cart.total == 2382.5


def test_point_discount():
    items = [Item("T-Shirt", 350, "Clothing"), Item("Hat", 250, "Accessories"), Item("Belt", 230, "Accessories")]
    cart = Cart(items)
    discount = PointDiscount(68)
    print("Before applying discount, total is:", cart.total)
    cart.apply_discount([discount])
    print("Cart total after PointDiscount:", cart.total)
    assert cart.total == 762


def test_seasonal_discount():
    items = [Item("T-Shirt", 350, "Clothing"), Item("Hat", 250, "Accessories"), Item("Belt", 230, "Accessories")]
    cart = Cart(items)
    discount = SpecialDiscount(every_x=300, discount_y=40)
    print("Before applying discount, total is:", cart.total)
    cart.apply_discount([discount])
    print("Cart total after SpecialDiscount:", cart.total)
    assert cart.total == 750


def main():
    print("...Running test_fixed_discount...")
    test_fixed_discount()

    print("...Running test_percentage_discount...")
    test_percentage_discount()

    print("...Running test_category_percentage_discount...")
    test_category_percentage_discount()

    print("...Running test_point_discount...")
    test_point_discount()

    print("...Running test_seasonal_discount...")
    test_seasonal_discount()

    print("All tests passed!")


if __name__ == "__main__":
    main()
