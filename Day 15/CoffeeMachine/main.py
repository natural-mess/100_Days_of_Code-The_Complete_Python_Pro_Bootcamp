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

def prompt_user():
    return input("What would you like? (espresso/latte/cappuccino): ")

def print_report(current_resource):
    for key, value in current_resource.items():
        print(f"{key.capitalize()}: {value}{"ml" if key!="coffee" else "g"}")

def process_coin(coin_list):
    return coin_list["quarters"]*0.25 + coin_list["dimes"]*0.10 + coin_list["nickles"]*0.05 + coin_list["pennies"]*0.01

def check_resource(current_resource, menu, choice):
    resource_check_result = ''
    if choice not in menu.keys():
        resource_check_result = "invalid"
    else:
        choice_resource = menu[choice]["ingredients"]
        for key in choice_resource.keys():
            if current_resource[key] < choice_resource[key]:
                resource_check_result = key
                break

    return resource_check_result

def check_transaction(coin_list, menu, choice):
    inserted_money = process_coin(coin_list)
    cost = menu[choice]["cost"]
    if inserted_money == cost:
        return 0
    elif inserted_money < cost:
        return -1
    else:
        return inserted_money - cost

def init_coin_list():
    coin_list = {
        "quarters": 0.0,
        "dimes": 0.0,
        "nickles": 0.0,
        "pennies": 0.0
    }
    return coin_list

def update_resource(current_resource, menu, choice):
    for key in menu[choice]["ingredients"].keys():
        current_resource[key] -= menu[choice]["ingredients"][key]
    return current_resource

def coffee_machine():
    current_resource = resources.copy()
    menu = MENU.copy()
    machine_money = 0
    while 1:
        coin_list = init_coin_list()
        command = prompt_user()
        if command == "report":
            print_report(current_resource)
            print(f"Money: ${machine_money}")
        elif command == "off":
            exit()
        else:
            resource_check_result = check_resource(current_resource, menu, command)
            if resource_check_result == "invalid":
                print("Invalid command")
            elif resource_check_result == "":
                print("Please insert coins.")
                for key in coin_list.keys():
                    coin_list[key] = float(input(f"How many {key}?: "))
                transaction_result = check_transaction(coin_list, menu, command)
                if transaction_result < 0:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    if transaction_result > 0:
                        print(f"Here is ${round(transaction_result,2)} in change.")
                    machine_money += menu[command]["cost"]
                    print(f"Here is your {command}☕. Enjoy!")
                    current_resource = update_resource(current_resource, menu, command)
            else:
                print(f"Sorry, there is not enough {resource_check_result}.")

coffee_machine()
