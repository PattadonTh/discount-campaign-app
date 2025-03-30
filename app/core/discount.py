from abc import ABC, abstractmethod


class Discount(ABC):
    @abstractmethod
    def apply(self, items, total):
        pass


class FixedDiscount(Discount):
    def __init__(self, fixed_amount):
        self.fixed_amount = fixed_amount

    def apply(self, items, total):
        if total <= self.fixed_amount:
            return 0
        return total - self.fixed_amount


class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply(self, items, total):
        return total * (1 - (self.percentage / 100))


class CategoryPercentageDiscount(Discount):
    def __init__(self, category_percentage_discount):
        self.category_percentage_discount = category_percentage_discount

    def apply(self, items, total):
        for item in items:
            if item.category in self.category_percentage_discount:
                percentage = self.category_percentage_discount[item.category]
                item.price = item.price * (1 - (percentage / 100))
        return sum(item.price for item in items)


class PointDiscount(Discount):
    def __init__(self, point):
        self.point = point

    def apply(self, items, total):
        discount = min(0.2 * total, self.point)
        return total - discount


class SpecialDiscount(Discount):
    def __init__(self, every_x, discount_y):
        self.every_x = every_x
        self.discount_y = discount_y

    def apply(self, items, total):
        if self.every_x > total:
            return total
        discount = (total // self.every_x) * self.discount_y
        return total - discount
