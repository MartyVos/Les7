def ticker(filename):
    file = open(filename, "r")
    regel = len(file.readlines())
    file.seek(0)
    name = input("Enter Company name: ")
    temp = []
    temp2 = []
    compTick = {}
    for x in range(regel):
        temp.append(file.readline().split("\n")[0])
        temp2.append(temp[x].split(":"))
        compTick[temp2[x][0]] = temp2[x][1]

    if name in compTick.keys():
        print("Ticker symbol:", compTick.get(name), "\n")

    tick = input("Enter Ticker symbol: ")
    keys = list(compTick.keys())
    values = list(compTick.values())

    for y in range(len(compTick)):
        if tick in values[y]:
            print("Company name:", keys[y])
    file.close()


ticker("ticker_symbol.txt")
