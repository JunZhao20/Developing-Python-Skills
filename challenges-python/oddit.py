def find_it(seq):
    lst = set(seq)
    for i in lst:
        if seq.count(i) % 2 != 0 or seq.count(i) == 1:
            print(i)


find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5])
