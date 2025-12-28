MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 10,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def check_resources(choice):
    """Checks if there are enough resources (water, milk, and coffee)"""
    # RESOURCES
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    # MENU
    espresso = MENU["espresso"]["ingredients"]
    latte = MENU["latte"]["ingredients"]
    cappuccino = MENU["cappuccino"]["ingredients"]

# Used hard coded values but changed to values in dictionary for flexibility
    if choice == "espresso":
        if water >= espresso["water"] and coffee >= espresso["coffee"]:
            sufficient_resources = True
            return sufficient_resources
        elif water < espresso["water"]:
            print("Not enough water\n")
            return False
        elif coffee < espresso["coffee"]:
            print("Not enough milk\n")
            return False
    elif choice == "latte":
        if water >= latte["water"] and milk >= latte["milk"] and coffee >= latte["coffee"]:
            sufficient_resources = True
            return sufficient_resources
        elif water < latte["water"]:
            print("Not enough water\n")
            return False
        elif milk < latte["milk"]:
            print("Not enough milk\n")
            return False
        elif coffee < latte["coffee"]:
            print("Not enough coffee\n")
            return False
    elif choice == "cappuccino":
        if water >= cappuccino["water"] and milk >= cappuccino["milk"] and coffee >= cappuccino["coffee"]:
            sufficient_resources = True
            return sufficient_resources
        elif water < cappuccino["water"]:
            print("Not enough water\n")
            return False
        elif milk < cappuccino["milk"]:
            print("Not enough milk\n")
            return False
        elif coffee < cappuccino["coffee"]:
            print("Not enough coffee\n")
            return False

def process_coins(choice, q, d, n, p):
    """Calculates coins and change if any"""
    qtr = q * 0.25
    dme = d * 0.10
    nkl = n * 0.05
    pen = p * 0.01

    espresso_cost = MENU["espresso"]["cost"]
    latte_cost = MENU["latte"]["cost"]
    cappuccino_cost = MENU["cappuccino"]["cost"]
    money = resources["money"]

    total = round(qtr + dme + nkl + pen, 2)
    if total == espresso_cost:
        money += total
        change = 0
        return change, True
    elif total > espresso_cost:
        money += total
        change = round(total - espresso_cost, 2)
        return change, True
    elif total < espresso_cost:
        print("Sorry that's not enough money. Money refunded")
    elif total == latte_cost:
        money += total
        change = 0
        return change, True
    elif total > latte_cost:
        money += total
        change = round(total - latte_cost, 2)
        return change, True
    elif total > latte_cost:
        print("Sorry that's not enough money. Money refunded")
    elif total == cappuccino_cost:
        money += total
        change = 0
        return change, True
    elif total > cappuccino_cost:
        money += total
        change = round(total - latte_cost, 2)
        return change, True
    elif total > cappuccino_cost:
        print("Sorry that's not enough money. Money refunded")

def make_item(selection):
    """Makes the ordered item"""
    # RESOURCES -> I learned this does not and cannot actually update the resources.
    # The way I am doing this is just local variables (int) and I need to actually reference the dictionary.
    # water = resources["water"]
    # milk = resources["milk"]
    # coffee = resources["coffee"]

    # MENU
    espresso = MENU["espresso"]["ingredients"]
    latte = MENU["latte"]["ingredients"]
    cappuccino = MENU["cappuccino"]["ingredients"]

    if selection == "espresso":
        resources["water"] -= espresso["water"]
        resources["coffee"] -= espresso["coffee"]
    elif selection == "latte":
        resources["water"] -= latte["water"]
        resources["milk"] -= latte["milk"]
        resources["coffee"] -= latte["coffee"]
    elif selection == "cappuccino":
        resources["water"] -= cappuccino["water"]
        resources["milk"] -= cappuccino["milk"]
        resources["coffee"] -= cappuccino["coffee"]

off = False

while not off:
    print("Espresso: $1.50, Latte: $2.50, Cappuccino: $3.50")
    selection = input("What would you like? (espresso, latte, cappuccino): ")
    if selection == "report":
        print("\n======== Report =======")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}\n")
    elif selection == "off":
        off = True

    if check_resources(selection) == True:
        print("Please insert coins.")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickles = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))
        change, item_made = process_coins(selection, quarters, dimes, nickles, pennies)
        if change != 0:
            print(f"Here is ${change} in change.")
        if item_made == True:
            make_item(selection)
            print(f"Here is your {selection} ☕. Enjoy!")
