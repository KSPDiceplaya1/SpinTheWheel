import random
import time
import subprocess
global guesses
guesses = 1
name = input("What is your name? -")
print(name, "Hello, welcome")
subprocess.call(["afplay", "Fietsbel.wav"])
time.sleep(.5)
print("Reminder: Think of the Earth from top to bottom and think of the positioning.")
time.sleep(1)
sysNum = random.randint(0,100)
def end():
    print("Good Bye, come back next time")
def userGuess():
    userNum = input("I am thinking of a number, What is your guess?: ")
    global guesses
    guesses += 1
    print(" Guesses so far:", guesses)
    if sysNum == int(userNum):
        print("You are at the Equator.")
        time.sleep(1)
        print("You got is right")
        end()
    elif sysNum > (int(userNum)):
        print("You are in Antarctica. Try again.")
        time.sleep(2)
        userGuess()
    elif sysNum < (int(userNum)):
        print("You are at the North Pole. Try again.")
        time.sleep(2)
        userGuess()
userGuess()

