aantal = 0
getal = 1
som = 0

while getal != 0:
    getal = eval(input("Geef een getal: "))
    som = som + getal
    aantal += 1
print("Er zijn", aantal - 1, "getallen ingevoerd, de som is:", som)
