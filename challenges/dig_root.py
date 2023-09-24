def digital_root(n):
    lst = list(map(int, str(n)))
    lst = sum(lst)
    while lst > 9:
        lst = list(map(int, str(lst)))
        lst = sum(lst)
        
    else:
        return lst
    
        
        
    
print(digital_root(493193))