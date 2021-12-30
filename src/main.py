from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker(menu)
money_machine = MoneyMachine(menu,coffee_maker)


if not coffee_maker.machine_state():
	#if machine is off
	coffee_maker.start()

is_on = coffee_maker.machine_state()

options_available = ""
for item in menu.get_items():
	options_available += (item + "/")

print("#"*30)
print("COFFEE MACHINE")
print("#"*30)

while is_on:
	choice = input(f"What you would like to have {options_available} ?")
	if choice == "off":
		is_on = coffee_maker.stop()
	elif choice == "report":
		coffee_maker.report()
		print("\n")
		money_machine.report()
	else:
		drink = choice
		if not menu.find_item(drink):
			print("Drink not Available")
		else:
			is_resources_sufficient = coffee_maker.is_resource_available(drink)
			if is_resources_sufficient:
				is_money_sufficient = money_machine.make_payment(drink)
				if is_money_sufficient:
					coffee_maker.make_coffee(drink)

