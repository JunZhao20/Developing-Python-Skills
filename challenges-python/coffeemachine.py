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

money = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickle": 0.05,
    "penny": 0.01
}


def process_money(info):
    quarters = float(input("How many quarters?: "))
    info["Money"] += quarters*money['quarter']
    dimes = float(input("How many dimes?: "))
    info["Money"] += dimes*money['dime']
    nickles = float(input("How many nickles?: "))
    info["Money"] += nickles*money['nickle']
    pennies = float(input("How many pennies?: "))
    info["Money"] += pennies*money['penny']


def check_resource_latte(info):
    water = info['Water'] >= MENU['latte']['ingredients']['water']
    milk = info['Milk'] >= MENU['latte']['ingredients']['milk']
    coffeeIng = info['Coffee'] >= MENU['latte']['ingredients']['coffee']
    cash = info['Money'] >= MENU['latte']['cost']

    if water and milk and coffeeIng and cash:
        info['Water'] -= MENU['latte']['ingredients']['water']
        info['Milk'] -= MENU['latte']['ingredients']['milk']
        info['Coffee'] -= MENU['latte']['ingredients']['coffee']
        info['Money'] -= MENU['latte']['cost']
        print(f"your change: {round(info['Money'])}")
    elif water != True:
        print("no water")
    elif milk != True:
        print("no milk")
    elif coffeeIng != True:
        print("no coffee")
    elif cash != True:
        print("no cash")


def check_resource_espresso(info):
    water = info['Water'] >= MENU['espresso']['ingredients']['water']
    coffeeIng = info['Coffee'] >= MENU['espresso']['ingredients']['coffee']
    cash = info['Money'] >= MENU['espresso']['cost']

    if water and coffeeIng and cash:
        info['Water'] -= MENU['espresso']['ingredients']['water']
        info['Coffee'] -= MENU['espresso']['ingredients']['coffee']
        info['Money'] -= MENU['espresso']['cost']
        print(f"your change: {round(info['Money'])}")
    elif water != True:
        print("no water")
    elif coffeeIng != True:
        print("no coffee")
    elif cash != True:
        print("no cash")


def check_resource_cappuccino(info):
    water = info['Water'] >= MENU['cappuccino']['ingredients']['water']
    milk = info['Milk'] >= MENU['cappuccino']['ingredients']['milk']
    coffeeIng = info['Coffee'] >= MENU['cappuccino']['ingredients']['coffee']
    cash = info['Money'] >= MENU['cappuccino']['cost']

    if water and milk and coffeeIng and cash:
        info['Water'] -= MENU['cappuccino']['ingredients']['water']
        info['Milk'] -= MENU['cappuccino']['ingredients']['milk']
        info['Coffee'] -= MENU['cappuccino']['ingredients']['coffee']
        info['Money'] -= MENU['cappuccino']['cost']
        print(f"your change: {round(info['Money'])}")
    elif water != True:
        print("no water")
    elif milk != True:
        print("no milk")
    elif coffeeIng != True:
        print("no coffee")
    elif cash != True:
        print("no cash")


def coffee_machine():
    off = False
    info = {
        "Water": 300,
        "Milk": 200,
        "Coffee": 100,
        "Money": float(0)
    }
    while off != True:
        coffee = input("What would you like (latte/cappuccino/espresso)?: ")

        if coffee == 'off':
            off = True
            break
        elif coffee == 'report':
            print(
                f"Water: {info['Water']}ml\nMilk: {info['Milk']}ml\nCoffee: {info['Coffee']}g\nMoney: ${info['Money']}")
        elif coffee == 'latte':
            print("Insert coins")
            process_money(info=info)
            check_resource_latte(info=info)
        elif coffee == 'espresso':
            print("Insert coins")
            process_money(info=info)
            check_resource_espresso(info=info)
        elif coffee == 'cappuccino':
            print("Insert coins")
            process_money(info=info)
            check_resource_cappuccino(info=info)


coffee_machine()
