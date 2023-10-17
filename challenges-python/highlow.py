def high_and_low(numbers):
    numbers = numbers.split()
    lst = []

    for i in numbers:
        lst.append(int(i))

    return f"{max(lst)} {min(lst)}"


high_and_low("1 -2 3 4 5")
