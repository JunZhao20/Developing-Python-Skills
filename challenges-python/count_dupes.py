def duplicate_count(text):
    string = [i.lower() for i in text]
    unique = set(string)
    count = 0
    for x in unique:
        num = string.count(x)
        if num >= 2:
            count += 1
    return count
        
    
    
print(duplicate_count('aAbb'))