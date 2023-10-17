import math

pi = math.pi

lst = []


def sort_of_area(seq):

    for i in seq:
        if type(i) == tuple:
            lst.append(round(i[0] * i[1], 2))
        else:
            lst.append(round(pi*i**2, 2))

    print(lst.sort(key=float))
    """
    return seq.sort(key=sort_of_area)
"""


sort_of_area([(4.23, 6.43), 1.23, 3.444, (1.342, 3.212)])
