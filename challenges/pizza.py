
size = input("What size pizza do you want (S, M or L)? ")
pepperoni = input("Do you want to add pepperoni (Y or N)? ")
cheese = input("Do you want to add cheese (Y or N)? ")
bill = 0

if size == 'S':
    bill += 15
    if pepperoni == 'Y':
        bill += 2
    else:
        bill += 0
    if cheese == 'Y':
        bill += 1
    else:
        bill += 0

elif size == 'M':
    bill += 20
    if pepperoni == 'Y':
        bill += 3
    else:
        bill += 0
    if cheese == 'Y':
        bill += 1
    else:
        bill += 0

elif size == 'L':
    bill += 25
    if pepperoni == 'Y':
        bill += 3
    else:
        bill += 0
    if cheese == 'Y':
        bill += 1
    else:
        bill += 0

else:
    print("invalid order")

print(bill)
