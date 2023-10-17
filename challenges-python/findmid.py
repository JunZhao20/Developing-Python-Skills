
def get_middle(s):
    count = 0
    string = ""

    for i in s:
        count += 1

    half = count/2

    if count % 2 == 0:
        string += s[int(half)-1]
        string += s[int(half)]
        return string
    else:
        half = half-0.5
        string += s[int(half)]
        return string
