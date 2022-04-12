
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


# def return_drink(order):
#     """This function grabs the drink in a more readable format. Returns cost, water, coffee, milk in that order"""
#
#     return drink

def display_resources():
    """Mostly for when report is entered as an input, prints the resources in a easily readable state"""
    water = resources["water"]
    coffee = resources["coffee"]
    milk = resources["milk"]
    money = resources["money"]
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")

# Angela uses a for loop to loop through the resources dictionary and compare it with the order.
# She also used a separate variable for money. I can't use a loop since I have money in the resources.


def enough_water(water):
    """Compares water needed for order with resources, returns True if there's enough"""
    if resources["water"] >= water:
        return True
    else:
        return False


def enough_coffee(coffee):
    if resources["coffee"] >= coffee:
        return True
    else:
        return False


def enough_milk(milk):
    if resources["milk"] >= milk:
        return True
    else:
        return False


def get_coins():
    """Asks how many coins the user wants to put in and returns the total"""
    print("Feed me some coins bruh")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    # print(f"{quarters} quarters + {dimes} dimes + {nickels} nickels + {pennies} pennies is {total:.2f}")  # for debug
    print(f"You put in ${total}.")
    return total


def machine_on():
    order = input("What would you like? (Espresso - $1.50/Latte - $2.50/Cappuccino - $3.00): ").lower()
    if order == 'off':
        return
    elif order == 'report':
        display_resources()
    elif order in MENU:
        cost = MENU[order]["cost"]
        water = MENU[order]["ingredients"]["water"]
        coffee = MENU[order]["ingredients"]["coffee"]
        if order != 'espresso':
            milk = MENU[order]["ingredients"]["milk"]
        else:
            milk = 0
        # drink = [cost, water, coffee, milk]
        # having all these nested loops is pretty janky, Angela separates a lot of it into different functions
        # eg. is_resource_sufficient, is_transaction_successful, make_coffee
        if enough_water(water):
            if enough_coffee(coffee):
                if enough_milk(milk):
                    # print("nice there's enough of everything")
                    pay = get_coins()
                    if pay >= cost:
                        change = pay - cost  # money returned to customer
                        resources["money"] += cost  # adds money to resources
                        resources["water"] -= water
                        resources["coffee"] -= coffee
                        resources["milk"] -= milk  # This is not DRY code, too lazy to refactor rn tho
                        if pay != cost:
                            print(f"Here's your ${change:.2f} change.")
                        print(f"Here's your {order} ☕. Enjoy!")
                    else:
                        print("that ain't enough cash dude")
                else:
                    print("not enough milk")
            else:
                print("not enough coffee")
        else:
            print("not enough water")
    else:
        print("Give me a valid input yo.")

    machine_on()


machine_on()
