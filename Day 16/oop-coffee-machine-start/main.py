from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

items = Menu()
money = MoneyMachine()
coffee = CoffeeMaker()

while True:
    choice = input(f"What would you like? ({items.get_items()}): ")
    if choice == "report":
        coffee.report()
        money.report()
    elif choice == "off":
        exit()
    else:
        drink = items.find_drink(choice)
        # Solution only uses coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost)
        # But if user types an option which is not in the menu, program will stop with error :
        # AttributeError: 'NoneType' object has no attribute 'ingredients'
        # So adding a condition for drink will avoid this issue and keep the program running
        if drink and coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee.make_coffee(drink)

