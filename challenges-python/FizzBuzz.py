
for i in range(1, 101):
    if i % 3 == 0:
        i = "Fizz"
        print(f"{i}")
    elif i % 5 == 0:
        i = "Buzz"
        print(f"{i}")
    elif i % 3 == 0 and i % 5 == 0:
        i = "FizzBuzz"
        print(f"{i}")
    else:
        print(i)
