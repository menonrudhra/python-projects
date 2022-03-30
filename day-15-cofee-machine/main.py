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
    "water": 500,
    "milk": 200,
    "coffee": 100,
}

money = 0

COINS = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01
}


# TODO: 3. Print report.
#  a. When the user enters “report” to the prompt, a report should be generated that shows
#  the current resource values.
def print_report():
    print(f"Water: {resources['water']}mL")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


# TODO: 4. Check resources sufficient? When the user chooses a drink, the program should check if there are enough
#  resources to make that drink.
def is_sufficient_resource(user_choice):
    for ingredient in MENU[user_choice]["ingredients"]:
        balance = resources[ingredient] - MENU[user_choice]["ingredients"][ingredient]
        if balance < 0:
            print(f"Sorry, there is not enough {ingredient}")
            return False
    return True


# TODO: 5. Process coins. If there are sufficient resources to make the drink selected, then the program should
#  prompt the user to insert coins
def process_coins():
    print("Please insert coins.")
    total_amount = 0
    for coin in COINS:
        number_of_coins = int(input(f"how many {coin}s?: "))
        total_amount += (number_of_coins * COINS[coin])
    return round(total_amount, 2)


# TODO: 6. Check transaction successful? Check that the user has inserted enough money to purchase the drink they
#  selected.
def is_successful_transaction(amount, user_choice):
    cost_of_coffee = MENU[user_choice]["cost"]
    if cost_of_coffee > amount:
        print(f"Sorry that's not enough money. Price of {user_choice} is ${cost_of_coffee}, but you paid ${amount}. Money "
              f"refunded.")
        return False
    else:
        balance = round(amount - cost_of_coffee, 2)
        global money
        money += cost_of_coffee
        print(f"You paid: {amount}. Price of {user_choice} is {cost_of_coffee}.")
        print(f"Here is ${balance} in change.")
        return True


# TODO: 7. Make Coffee. If the transaction is successful and there are enough resources to make the drink the user
#  selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
def make_coffee(user_choice):
    global resources
    for ingredient in MENU[user_choice]["ingredients"]:
        resources[ingredient] = resources[ingredient] - MENU[user_choice]["ingredients"][ingredient]
    print(f"Here is your {user_choice} ☕. Enjoy!")


def coffee_machine():
    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt. Your code should end execution when this
    #  happens.
    turn_off = False
    while not turn_off:
        # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino): The prompt should show
        #  every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve
        #  the next customer.
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == "off":
            turn_off = True
        elif user_choice == "report":
            print_report()
        elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
            if is_sufficient_resource(user_choice):
                total = process_coins()
                if is_successful_transaction(total, user_choice):
                    make_coffee(user_choice)

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    coffee_machine()
