from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

off = False

while not off:
    selection = input(f"What would you like? {menu.get_items()}? ").lower()
    if selection == "off":
        off = True
    elif selection == "report":
        print("\nReporting...")
        coffee_maker.report()
        money_machine.report()
        print("\n")
    else:
        drink = menu.find_drink(selection)
        sufficient = coffee_maker.is_resource_sufficient(drink)
        if sufficient:
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)
