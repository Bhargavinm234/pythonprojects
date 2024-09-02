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
}

def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is no enough {item}")
            return False
    return True


def process_coins():
    """Returns the total of coins inserted"""
    print("Please insert coins:")
    total = int(input("How many quarters?:"))*0.25
    total += int(input("How many dimes?:")) * 0.1
    total += int(input("How many nickles?:")) * 0.05
    total += int(input("How many pennies?:")) * 0.01
    return total


def is_transaction_successfull(amount_recieved , drink_cost,):
    """Return true when payment is accepted , else false"""
    if amount_recieved >= drink_cost:
        change =round(amount_recieved - drink_cost,2)
        global profit
        profit+= drink_cost
        print(f"Here is ${change} in change")
        return True
    else:
        print("Sorry that's not enough money !! Money is returned")
        return False


def make_coffee(drink_name , ingredients):
    """Deduct the required ingredients from the resources"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}")



is_on = True
profit = 0
while is_on:
    user_choice = input("What would you like (expresso/latte/cappuccino)?")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print(f"Water: {resources["water"]} ml")
        print(f"Milk: {resources["milk"]} ml")
        print(f"Coffee: {resources["coffee"]} ml")
        print(f"Profit: {profit}")
    else:
        drink = MENU[user_choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successfull(payment, drink["cost"]):
                make_coffee(user_choice,drink["ingredients"])






