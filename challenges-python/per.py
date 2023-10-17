lst = []


def per(n):
    n = list(str(n))
    n2 = []
    for i in n:
        i = int(i)
        n2.append(i)
    print(n2)

    while n2.count(0) != 0:
        total = int(n2[0]) * int(n2[1])
        lst.append(total)

        print(lst)


per(23)
