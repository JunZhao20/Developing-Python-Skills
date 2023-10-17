def array_diff(a, b):
    for i in a:
        for i in b:
            while a.count(i) != 0:
                a.remove(i)
            
    return a

print(array_diff([1,2,2], [1]))