class Menu:
	
	def __init__(self):
		self.menu = [
			{
				"name":"espresso",
				"ingredients":{
					"water":50,
					"coffee":18
				},
				"cost":1.5
			},
			{
				"name":"latte",
				"ingredients":{
					"water":200,
					"coffee":24,
					"milk":150
				},
				"cost":2.5
			},
			{
				"name":"cappuccino",
				"ingredients":{
					"water":250,
					"coffee":24,
					"milk":100
				},
				"cost":3.0
			}

		]


	def get_items(self):
		"""Return name of items present in menu"""
		items = []
		for item in self.menu:
			items.append(item['name'])
		return items


	def get_item_detail(self, item):
		"""Return details of the item mentioned"""
		for _item in self.menu:
			if item == _item['name']:
				return _item



	def find_item(self, item):
		"""Return True if item is present in menu list"""
		items = self.get_items()
		if item in items:
			return True
		return False


	def get_ingredients_of_item(self, item):
		"""Return ingredients required to make the item"""
		if self.find_item(item):
			#item is present in menu
			item_detail = self.get_item_detail(item)
			return item_detail['ingredients']


	def get_cost_of_item(self, item):
		"""Return cost required to make the item"""
		if self.find_item(item):
			#item is present in menu
			item_detail = self.get_item_detail(item)
			return item_detail['cost']
 


"""
menu = [
	{
	 'name': 'espresso',
	 'ingredients': {'water': 50, 'coffee': 18},
	 'cost': 1.5
	}, 

	{'name': 'latte', 
	 'ingredients': {'water': 200, 'coffee': 24, 'milk': 150},
	 'cost': 2.5
	},

	{'name': 'espresso',
	 'ingredients': {'water': 250, 'coffee': 24, 'milk': 100}, 
	 'cost': 3.0
	}
]

"""