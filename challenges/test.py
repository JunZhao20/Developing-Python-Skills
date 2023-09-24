

"""
def create_dict(keys, value):

    dic = dict.fromkeys(keys)
    for o in value:
        dic.update({dic.keys(): o})

    print(dic)


create_dict(['a', 'b', 'c', 'd'], [1, 2, 3])
"""


"""lst = [1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]
newlst = set(lst)
for i in newlst:
    if lst.count(i) % 2 != 0 or lst.count(i) == 1:
        pass"""


"""def bouncing_ball(h, bounce, window):
    if (h > 0) and (bounce > 0 and bounce < 1) and (window < h):
        print(round((h/bounce) - window))
    else:
        return -1


bouncing_ball(30, 0.66, 1.5)"""

"""MENU = {
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

print(MENU['espresso']['ingredients']['water'])

info = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": float(5)
}

water = info['Water'] >= MENU['latte']['ingredients']['water']
milk = info['Milk'] >= MENU['latte']['ingredients']['milk']
coffeeIng = info['Coffee'] >= MENU['latte']['ingredients']['coffee']
cash = info['Money'] >= MENU['latte']['cost']

if water and milk and coffeeIng and cash:
    info['Water'] -= MENU['latte']['ingredients']['water']
    info['Milk'] -= MENU['latte']['ingredients']['milk']
    info['Coffee'] -= MENU['latte']['ingredients']['coffee']
    info['Money'] -= MENU['latte']['cost']
    print(f"your change: {info['Money']}")
elif water != True:
    print("no water")
elif milk != True:
    print("no milk")
elif coffeeIng != True:
    print("no coffee")
elif cash != True:
    print("no cash")"""

"""seq = 'sdfs:)'
print(seq.isnumeric(), seq.isalpha())


def count_smileys(arr):
    count = 0

    for face in arr:
        for f in face:
            if f.isnumeric() != True or f.isalpha() != True:
                print(f.isnumeric(), f.isalpha())
                if face.count(':') == 1 or face.count(';') == 1:
                    if face.count('D') == 1 or face.count(')') == 1:
                        if face.count('-') < 2 and face.count('~') < 2:
                            if face.isnumeric() == False:
                                count += 1

    print(count)


count_smileys(["x2yz:-)", ":-2)xyz", ":---)"])"""

lst = [1,2,3]

if 1 in lst:
    print(True)
else:
    print(False)