from .item import Item
from .discount import Discount


class Cart:
    def __init__(self, items: list[Item]):
        self.items = items
        self.total = sum(item.price for item in items)

    def apply_discount(self, discounts: list[Discount]):
        for discount in discounts:
            self.total = discount.apply(self.items, self.total)
        return round(self.total, 2)
