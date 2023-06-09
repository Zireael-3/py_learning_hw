"""
You are given the following code:

class Order:
    morning_discount = 0.25

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price - self.price * self.morning_discount

Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy

Example of the result call:

def morning_discount(order):
    ...

def elder_discount(order):
    ...

order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50

order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10
"""


class DiscountStrategy:
    def apply_discount(self, price):
        pass


# Next, we can define concrete discount strategies, such as MorningDiscount and ElderDiscount:

class MorningDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.25


class ElderDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.5


# Finally, we can modify the Order class to take a discount strategy object as a parameter to its constructor:

class Order:
    def __init__(self, price, discount_strategy):
        self.price = price
        self.discount_strategy = discount_strategy

    def final_price(self):
        return self.price - self.discount_strategy.apply_discount(self.price)


# Now, we can create an Order object with a specific discount strategy
# and call its final_price method to get the discounted price:

order_1 = Order(100, MorningDiscount())
assert order_1.final_price() == 75

order_2 = Order(100, ElderDiscount())
assert order_2.final_price() == 50
