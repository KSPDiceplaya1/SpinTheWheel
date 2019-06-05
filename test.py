import random
import time
import subprocess
wrong = 0
Money = 200
times = 0
numCar = 0
tripid = ""
#start of the program
def start():
    print("888       888 888                        888       .d88888b.   .d888      8888888888           88888888888                            ")
    print("888   o   888 888                        888      d88P   Y88b d88P        888                      888                                ")
    print("888  d8b  888 888                        888      888     888 888         888                      888                                ")
    print("888 d888b 888 88888b.   .d88b.   .d88b.  888      888     888 888888      8888888  .d88b.  888d888 888  888  888 88888b.   .d88b.     ")
    print("888d88888b888 888  88b d8P  Y8b d8P  Y8b 888      888     888 888         888     d88  88b 888P    888  888  888 888  88b d8P  Y8b    ")
    print("88888P Y88888 888  888 88888888 88888888 888      888     888 888         888     888  888 888     888  888  888 888  888 88888888    ")
    print("8888P   Y8888 888  888 Y8b.     Y8b.     888      Y88b. .d88P 888         888     Y88..88P 888     888  Y88b 888 888  888 Y8b.        ")
    print("888P     Y888 888  888   Y8888    Y8888  888        Y88888P   888         888       Y88P   888     888    Y88888 888  888   Y8888     ")

    time.sleep(3)

    #Menu
    print("Welcome to Wheel of Fortune!   ")
    print("This program was created by Brian Le and Christwide Oscar.  ")
    print("Welcome To the new version of PyWheel ")


    def userinfo():
        username = input("What is your name?:")
        print("Hello! " + username +". \n")
        song = input("What is your favorite song?:")
        print(song + ", I love that song also!")
        subject = input("Favorite subject?:")
        print(subject + ": Eww! I hate that subject.")
        print("Now get in to the game.")
        time.sleep(2)
    userinfo()
    print("   ")
    print("Lets play the game now! \n ")
    print("Lets get Started!\n")
    time.sleep(3)
    print("Entering the stage\n")
    time.sleep(2)
    print("loading\n")
    time.sleep(2)
    print("...\n")
    time.sleep(2)
    print("Loading ...\n")
    time.sleep(4)
    print("Script loaded.\n")
    time.sleep(1)
    program()
#the end of program if user loses
def end():
    print("game over")
    global username
    print(" Thnaks for playing the Game")
    print(" Goodbye see you soon!!  ")
    print("888       888 888                        888       .d88888b.   .d888      8888888888           88888888888                            ")
    print("888   o   888 888                        888      d88P   Y88b d88P        888                      888                                ")
    print("888  d8b  888 888                        888      888     888 888         888                      888                                ")
    print("888 d888b 888 88888b.   .d88b.   .d88b.  888      888     888 888888      8888888  .d88b.  888d888 888  888  888 88888b.   .d88b.     ")
    print("888d88888b888 888  88b d8P  Y8b d8P  Y8b 888      888     888 888         888     d88  88b 888P    888  888  888 888  88b d8P  Y8b    ")
    print("88888P Y88888 888  888 88888888 88888888 888      888     888 888         888     888  888 888     888  888  888 888  888 88888888    ")
    print("8888P   Y8888 888  888 Y8b.     Y8b.     888      Y88b. .d88P 888         888     Y88..88P 888     888  Y88b 888 888  888 Y8b.        ")
    print("888P     Y888 888  888   Y8888    Y8888  888        Y88888P   888         888       Y88P   888     888    Y88888 888  888   Y8888     ")

    print("  ")
    exit()
#restart the game 3 times for the user to play
def restart():
    time.sleep(2)
    print("You will play the game again. \n")
    program()
#user checking inventory
def inventory():
    print(numCar, "car(s)")
    print("You have one trip to:" + tripid)
#user is buying the trip that they want
def checktrip():
    global tripid
    global check
    print("What trip do you want?")
    print("1 - France       2 - Spain")
    usertrip = input("Trip:")
    if usertrip == "1":
        tripid = France
        check()
    elif usertrip == "2":
        tripid = Spain
        check()
#checks if user wants to buy again
def check():
    print("Yes - 1         No - 2")
    print("Inventory - 3")
    repeat = input("Do you want to buy again or check inventory?")
    if repeat == "1":
        shop()
    elif repeat == "2":
        exit()
    elif repeat == "3":
        inventory()
#the shop of the game to buy from
def shop():
    print("Car - 1           Trip - 2        I want more money - 3")
    print("Car - $2000       Trip - $3000")
    global Money
    print(Money)
    userBuy = input("What do you want to buy?  -")
    if userBuy == "1":
        Money -= 2000
        global numCar
        numCar += 1
        time.sleep(1)
        check()
    elif userBuy == "2":
        Money -=3000
        checktrip()
        time.sleep(1)
    elif userBuy == "3":
        print("Restarting game.")
        time.sleep(1)
        program()
#main working program
def program():
    pick = random.randint(1,8)
    if pick == 1:
        word = ['D','O','N','A','L','D',' ','T','R','U','M','P']
        guessword =['D','?','?','A','?','?',' ','T','?','?','?','P']
        wordC = "DONALD TRUMP"
        numlet = 12
    elif pick == 2:
        word = ['B','E','R','N','I','E',' ','S','A','N','D','E','R','S']
        guessword =['?','E','?','N','?','?',' ','?','?','N','?','?','?','?']
        wordC = "BERNIE SANDERS"
        numlet = 14
    elif pick == 3:
        word = ['K','A','N','Y','E',' ','W','E','S','T']
        guessword =['?','?','N','?','?',' ','?','?','S','T']
        wordC = "KANYE WEST"
        numlet =10
    elif pick == 4:
        word = ['B','A','R','A','C','K',' ','O','B','A','M','A']
        guessword =['?','A','?','?','C','K',' ','?','?','?','?','A']
        wordC = "BARACK OBAMA"
        numlet = 10
    elif pick == 5:
        word = ['H','O','U','S','T','O','N']
        guessword = ['H','?','U','?','T','?','?']
        wordC = "HOUSTON"
        numlet = 7
    elif pick == 6:
        word = ['S','E','A','T','T','L','E']
        guessword = ['?','?','A','?','?','?','E']
        wordC = "SEATTLE"
        numlet = 7
    elif pick == 7:
        word = ['P','E','R','U']
        guessword = ['P','?','R','U']
        wordC = "PERU"
        numlet = 4
    elif pick == 8:
        word = ['D','A','R','W','I','N']
        guessword = ['D','?','R','?','I','?']
        wordC = "DARWIN"
        numlet = 6

    while word != guessword:
        test = str(guessword)
        test2 = str(numlet)
        test3 = test.replace(",", "")
        test4 = test3.replace("\'", "")
        test5 = test4.replace("[", "")
        test6 = test5.replace("]", "")
        test7 = test6.replace(" ", " ")
        print(test2 + " letters  -  The hidden word is " + test7 + "\n")
        userguess = input("Take your guess at a letter:  " + "\n" )
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
        print("The word was", wordC)
        print("You got it right")
        global times
        times += 1
        if times < 3:
            restart()
        elif times >= 3:
            print("Get ready for the final round.")
            time.sleep(3)
            final()
#final round program
def final():
    pick = random.randint(1,8)
    if pick == 1:
        word = ['B','Y','E','-','B','Y','E','-','B','Y','E']
        guessword =['B','?','E','-','B','Y','?','-','?','?','?']
        wordc = "Bye-Bye-Bye"
        numlet = 9
    elif pick == 2:
        word = ['L','O','V','E','-','Y','O','U','R','S','E','L','F']
        guessword =['?','?','V','?','-','Y','?','?','R','?','E','v','F']
        wordc = "Love Yourself"
        numlet = 12
    elif pick == 3:
        word = ['P','A','N','D','A']
        guessword =['P','?','N','?','A']
        wordc = "Panda"
        numlet = 5
    elif pick == 4:
        word = ['O','N','E','-','D','A','N','C','E']
        guessword = ['O','?','?','-','D','?','?','C','?']
        wordc = "One Dance"
        numlet = 8
    elif pick == 5:
        word = ['L','E','T','-','I','T','-','G','O']
        guessword = ['L','?','T','-','?','?','-','?','O']
        wordc = "Let it go"
        numlet = 7
    elif pick == 6:
        word = ['H','E','R','E']
        guessword = ['H','?','?','E']
        wordc = "Here"
        numlet = 4
    elif pick == 7:
        word = ['R','I','D','E']
        guessword = ['R','?','?','E']
        wordc = "Ride"
        numlet = 4
    elif pick == 8:
        word = ['I','-','W','A','N','N','A','-','K','N','O','W']
        guessword = ['I','-','W','?','?','?','?','-','?','N','?','W']
        wordc = "I wanna know"
        numlet = 10
    while word != guessword:
        test = str(guessword)
        test2 = str(numlet)
        test3 = test.replace(",", "")
        test4 = test3.replace("\'", "")
        test5 = test4.replace("[", "")
        test6 = test5.replace("]", "")
        test7 = test6.replace(" ", " ")
        print(test2 + " letters  -  The hidden word is " + test7 + "\n")
        userguess = input("Take your guess at a letter:  " + "\n")
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
            if wrong == 3:
                end()
    if word == guessword:
        print(wordc)
        print("The word was", wordc)
        print("You got it right")
        shop()
start()