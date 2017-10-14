while 1:
    woord = str(input("Geef een string van vier letter: "))
    if len(woord) != 4:
        lengte = len(woord)
        print(woord, "heeft", lengte, "letters")
    else:
        break
print("Inlezen van correcte string:", woord, "is geslaagd")
