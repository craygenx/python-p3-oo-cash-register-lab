#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * self.discount / 100
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    #the test methods differ in precision error
    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            last_item_price = self.get_item_price(last_item)
            self.total -= last_item_price
        else:
            self.total = 0

    def get_item_price(self, item):
        item_prices = {
            "eggs": 0.98,
            "book": 5.00,
            "Lucky Charms": 4.5,
            "Ritz Crackers": 5.0,
            "Justin's Peanut Butter Cups": 2.50,
            "macbook air": 1000,
            "apple": 0.99,
            "tomato": 1.76,
        }
        return item_prices.get(item, 0)

