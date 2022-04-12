from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
cha_ching = MoneyMachine()
machine_is_running = True

while machine_is_running:
    choices = menu.get_items()
    order = input(f"What would you like? ({choices}):").lower()

    if order == "off":
        print("smell ya later")
        machine_is_running = False
    elif order == "report":
        coffee_machine.report()
        cha_ching.report()
    else:
        drink = menu.find_drink(order)
        if (coffee_machine.is_resource_sufficient(drink)) and (cha_ching.make_payment(drink.cost)):
            print("ok got it")
            coffee_machine.make_coffee(drink)
