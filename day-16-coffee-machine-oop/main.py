from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == '__main__':
    menu = Menu()
    menu_items = menu.get_items()
    coffee_machine = CoffeeMaker()
    money_machine = MoneyMachine()

    turn_off = False
    while not turn_off:
        user_choice = user_choice = input(f"What would you like? ({menu_items}): ").lower()
        if user_choice == "off":
            turn_off = True
        elif user_choice == "report":
            coffee_machine.report()
            money_machine.report()
        else:
            menu_item_chosen = menu.find_drink(user_choice)
            if coffee_machine.is_resource_sufficient(menu_item_chosen) and money_machine.make_payment(menu_item_chosen.cost):
                coffee_machine.make_coffee(menu_item_chosen)

