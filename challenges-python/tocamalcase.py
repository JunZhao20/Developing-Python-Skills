def to_camel_case(text):
    sep = ''
    if text != "":
        for i in text:
            if i.isalpha() != True:
                sep += i
        text = text.translate({ord(i) : ' ' for i in sep})
        txt = text.split(' ')
        lst = [txt[x].capitalize() for x in range(1, len(txt))]
        lst.insert(0, txt[0])
        return ''.join(lst)
    return ""

print(to_camel_case("the_stealth-warrior_pet-cat"))