
year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0 and year % 400 == 0:
        print("leap year")
    elif year % 100 == 0 and year % 400 != 0:
        print("not leap year")
else:
    print("not leap year")
