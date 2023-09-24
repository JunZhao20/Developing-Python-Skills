

def calc():
    end = False

    while end != True:
        n1 = float(input("what is your first number?: "))
        print("+ \n-\n*\n/\n")
        op = input("Pick operation:")
        n2 = float(input("what is your second number?: "))

        dic = {
            "/": n1 / n2,
            "-": n1 - n2,
            "*": n1 * n2,
            "+": n1 + n2
        }

        ans = dic[op]
        print(ans)

        q = input("would you like to use this ans to calc 'y' or restart? 'r' ")
        if q == 'y':

            while q == 'y':
                dic = {
                    "/": ans / n2,
                    "-": ans - n2,
                    "*": ans * n2,
                    "+": ans + n2
                }
                print("+ \n-\n*\n/\n")
                op = input("Pick operation:")
                print(ans)
                n2 = float(input("what is your second number?: "))

                print(dic[op])
                q = input(
                    "would you like to use this ans to calc 'y' or restart? 'r' ")


print(calc())
