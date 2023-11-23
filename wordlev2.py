import colorama 
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

import random

word_list = ["wheel","basic","anger","carry","meant","rapid","lower",
             "fight","acute","chase","yield","visit","women","north","chose"]

picked_word = random.choice(word_list)

def verifyguess(guess):     # checks if word is a valid length
    return len(guess) == 5

def checkguess(guess):      #will check each letter in the picked word and compare it with the guessed word
    for i in guess:
        if i in picked_word:
            i = Back.GREEN + i
            return i

def wordledisplay():

    print(picked_word)      #displays the correct word for demonstration purposes

    guess = input("Enter your five-letter guess: ")     #User is prompted
    counter = 0
    maxcounter = 5
    while counter < maxcounter:

        if verifyguess(guess) == True:
            if guess == picked_word:
                print("Correct!")
                break
            elif guess != picked_word:
                checkguess(guess)
                return print(guess)
                            
        elif verifyguess(guess) == False:
            print("Enter a valid five-letter guess: ")
            continue
        counter += 1

wordledisplay()
