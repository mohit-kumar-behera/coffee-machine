from menu import Menu
from coffee_maker import CoffeeMaker

class MoneyMachine:

	def __init__(self, menu, coffee_maker):
		self.menu = menu
		self.coffee_maker = coffee_maker
		self.coin_values = {
			"quarters": 0.25,
      "dimes": 0.10,
      "nickles": 0.05,
      "pennies": 0.01
		}
		self.profit = 0
		self.money_recieved = 0


	def report(self):
		print(f"Todays Profit is ${self.profit}")


	def todays_profit(self):
		"""Todays Profit of the coffee machine"""
		print(f"Money : ${self.profit}") 


	def recieve_coin(self, item):
		"""Payment by the user"""
		print(f"Your drink costs ${self.menu.get_cost_of_item(item)}")
		print("Please Insert coins")
		for coin in self.coin_values:
			self.money_recieved += (int(input(f"How many {coin}? ")) * self.coin_values[coin])
		return self.money_recieved


	def make_payment(self, item):
		"""Process the payment and give back the change if customer gives excess money, Check if money is suffifcient or not"""
		self.recieve_coin(item)
		cost = self.menu.get_cost_of_item(item)
		money_recieved = self.money_recieved
		if money_recieved < cost:
			print(f"Your Order {item} is worth ${cost} and you have only paid ${round(money_recieved, 2)}.")
			print(f"We have refunded your paid ${round(money_recieved, 2)} amount")
			self.money_recieved = 0
			return False
		else:
			print(f"You paid a total of ${self.money_recieved}")
			change = round(self.money_recieved - cost, 2)
			print(f"Here is your ${change} in change")
			self.profit += cost
			self.money_recieved = 0
			return True

menu = Menu()
coffee_maker = CoffeeMaker(menu)
mm = MoneyMachine(menu,coffee_maker)

