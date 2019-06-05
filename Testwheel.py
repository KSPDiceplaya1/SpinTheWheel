import random
import time
import subprocess

wrong = 0
Money = 0
times = 0
def end():
    print("game over")
    exit()
def restart():
    time.sleep(2)
    print("You will play the game again. \n")
    program()
def final():
    pick = random.randint(1,2)
    if pick == 1:
        word = ['B','Y','E','-','B','Y','E','-','B','Y','E']
        guessword =['B','','E','-','B','Y','','-','','','']
    elif pick == 2:
        word = ['L','O','V','E','-','Y','O','U','R','S','E','L','F']
        guessword =['','','V','','-','Y','','','R','','E','','F']
    elif pick == 3:
        word = ['P','A','N','D','A']
        guessword =['P','','N','','A']
    elif pick == 4:
        word = ['O','N','E','-','D','A','N','C','E']
        guessword = ['O','','','-','D','','','C','']
    elif pick == 5:
        word = ['L','E','T','-','I','T','-','G','O']
        guessword = ['L','','T','-','','','-','','O']
    elif pick == 6:
        word = ['H','E','R','E']
        guessword = ['H','','','E']
    elif pick == 7:
        word = ['R','I','D','E']
        guessword = ['R','','','E']
    elif pick == 8:
        word = ['I','-','W','A','N','N','A','-','K','N','O','W']
        guessword = ['I','-','W','','','','','-','','N','','W']
    while word != guessword:
        print("The hidden word is", guessword)
        userguess = input("Take your guess at a letter:  ")
        userguess = userguess.upper()
        global Money
        global wrong
        print(wrong,"wrong")
        global money

        money = random.randint(1, 100)
        print("                                                                     You have $", Money + money)
        for letters in word:
            if userguess == letters:
                index = 0
                while index<len(word):
                    subprocess.call(["afplay", "pickup.wav"])
                    if word[index]== userguess:
                        guessword[index]=word[index]
                        Money += money
                    index += 1



        if word.count(userguess)== 0:
            wrong += 1
            subprocess.call(["afplay", "buzz.wav"])
            if wrong == 1:
                end()
    if word == guessword:
        print(word)
        print("The word was", word)
        print("You got it right")
        time.sleep(2)
        shop()
numCar = 0
numHouse = 0
def inventory():
    print(numCar, "car(s)")
def raman():
    print("Yes - 1         No - 2")
    print("Inventory - 3")
    repeat = input("Do you want to buy again or check inventory?")
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
def program():
    pick = random.randint(1,6)
    if pick == 1:
        word = ['D','O','N','A','L','D','-','T','R','U','M','P']
        guessword =['D','','','A','','','-','T','','','','P']
        numlet = 12
    elif pick == 2:
        word = ['B','E','R','N','I','E','-','S','A','N','D','E','R','S']
        guessword =['','E','','N','','','-','','','N','','','','']
        numlet = 14
    elif pick == 3:
        word = ['K','A','N','Y','E','-','W','E','S','T']
        guessword =['','','N','','','-','','','S','T']
        numlet =10
    elif pick == 4:
        word = ['B','A','R','A','C','K','-','O','B','A','M','A']
        guessword =['','','','','','','','','','']
        numlet = 10
    elif pick == 5:
        word = ['M','E','G']
        guessword = ['','','']
        numlet = 3
    elif pick == 6:
        word = ['P','R','E','S','T','O','N']
        guessword = ['','','','','','','']
        numlet = 7
    while word != guessword:
        print( numlet, "letters  -  The hidden word is", guessword,)
        userguess = input("Take your guess at a letter:  ")
        userguess = userguess.upper()
        global Money
        global wrong
        print(wrong,"wrong")
        global money

        money = random.randint(1, 100)
        print("                                                                     You have $", Money + money)
        for letters in word:
            if userguess == letters:
                subprocess.call(["afplay", "pickup.wav"])
                index = 0
                while index<len(word):
                    if word[index]== userguess:
                        guessword[index]=word[index]
                        Money += money
                    index += 1


        if word.count(userguess)== 0:
            wrong += 1
            Money -= money
            subprocess.call(["afplay", "buzz.wav"])
            if Money < 0:
                end()
    if word == guessword:
        print(word)
        print("The word was", word)
        print("You got it right")
        global times
        times += 1
        if times < 3:
            restart()
        elif times == 3:
            print("Get ready for the final round.")
            time.sleep(3)
            final()

program()