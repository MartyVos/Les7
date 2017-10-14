def namen():
    d = {}
    while 1:
        naam = input("Volgende naam: ")
        if naam not in d:
            d[naam] = 1
        else:
            d[naam] += 1
        key = list(d.keys())
        value = list(d.values())

        if naam == "":
            break

    key.pop()
    value.pop()

    for x in range(len(key)):
        if value[x] == 1:
            print("Er is", value[x], "student met de naam", key[x])
        else:
            print("Er zijn", value[x], "studenten met de naam", key[x])


namen()
