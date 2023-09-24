def count_smileys(arr):
    count = 0

    for face in arr:

        if face.count(':') == 1 or face.count(';') == 1:
            if face.count('D') == 1 or face.count(')') == 1:
                if face.count('-') < 2 and face.count('~') < 2:
                    if face.count(' ') == 0:
                        count += 1

        else:
            count += 0

    print(count)


count_smileys([":-)", ":-)xyz", ":---)"])
