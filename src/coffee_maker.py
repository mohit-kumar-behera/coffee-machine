from menu import Menu

class CoffeeMaker():

	def __init__(self,menu):
		self.is_on = False
		self.menu = menu
		self.resource = {
			"water":300,
			"milk":200,
			"coffee":100
		}


	def machine_state(self):
		"""Return wether the machine is on or off in True or False"""
		return self.is_on


	def start(self):
		"""Turn on the machine"""
		self.is_on = True
		return True


	def stop(self):
		"""Turn off the machine"""
		self.is_on = False
		return False


	def report(self):
		"""Print the resources available in the machine"""
		print(f"Water: {self.resource['water']}ml")
		print(f"Milk: {self.resource['milk']}ml")
		print(f"Coffee: {self.resource['coffee']}g")


	def is_resource_available(self,item):
		"""Return if the resources is sufficient to make the item or not"""
		can_make = True
		item_ingredients = self.menu.get_ingredients_of_item(item)
		for item_ingredient in item_ingredients:
			if self.resource[item_ingredient] < item_ingredients[item_ingredient]:
				print(f"{item_ingredient} left in machine is not enough to make {item}")
				can_make = False
		return can_make


	def make_coffee(self,item):
		item_ingredients = self.menu.get_ingredients_of_item(item)
		for item_ingredient in item_ingredients:
			self.resource[item_ingredient] -= item_ingredients[item_ingredient]
		print("~"*30)
		print(f"Here is your {item} ☕️. Enjoy!")
		print("~"*30)


menu = Menu()
cm = CoffeeMaker(menu)


		