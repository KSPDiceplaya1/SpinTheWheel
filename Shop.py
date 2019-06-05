global Money
Money = 10000
numCar = 0
numHouse = 0
def inventory():
    print(numCar, "car(s)")
def raman():
    print("Yes - 1         No - 2")
    print("Inventory - 3")
    repeat = input("Do you want to buy agian or check inventory?")
    if repeat == "1":
        shop()
    elif repeat == "2":
        exit()
    elif repeat == "3":
        inventory()

def shop():
    print("Car - 1           House - 2")
    print("Car - $2000       House - $3000")
    global Money
    print(Money)
    userBuy = input("What do you want to buy?  -")
    if userBuy == "1":
        Money -= 2000
        global numCar
        numCar += 1
        raman()
    elif userBuy == "2":
        money -=3000
        global numHouse
        numHouse += 1
        raman()
shop()