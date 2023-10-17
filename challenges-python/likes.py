def likes(names):
    if names == []:
        return "no one like this"
    if len(names) < 2:
        a = f"{names[0]} liked this"
        return a
    elif len(names) < 3:
        b = f"{names[0]} and {names[1]} liked this"
        return b
    elif len(names) < 4:
        c = f"{names[0]}, {names[1]} and {names[2]} liked this"
        return c
    elif len(names) >= 4:
        d = f"{names[0]}, {names[1]} and {len(names)-2} liked this"
        return d


likes([])
