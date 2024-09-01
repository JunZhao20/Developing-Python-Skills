def solution(s):
    string = list(s[1:len(s)])
    val = 0
    if s.islower() != True:
        for i in range(len(string)):
            if string[i+val].isupper():
                string.insert(i+val, ' ')
                val += 1
            
        return s[0] + ''.join(string)
    return ""
print(solution("camelCasing"))
print(solution("breakCamelCase"))