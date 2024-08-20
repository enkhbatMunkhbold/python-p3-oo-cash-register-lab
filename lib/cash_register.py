#!/usr/bin/env python3
class CashRegister:
  registered_items = []
  def __init__(self, dicscount = 0):
    self.discount = dicscount
    self.total = 0
    self.items = []
    self.transactions = []

  def add_item(self, item, price, quantity = 1):
    self.total += (price * quantity)
    self.transactions.append({"item": item, "price": price, "quantity": quantity})
    for _ in range(quantity):
      self.items.append(item)

  def apply_discount(self):
    if self.discount:
      self.total = int(self.total * ((100 - self.discount) / 100))
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print('There is no discount to apply.')

  def void_last_transaction(self):
    last_item = self.transactions[-1]
    self.total -= last_item['price'] * last_item['quantity']
    self.transactions.pop(-1)

# breakpoint()
     