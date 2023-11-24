import colorama 
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

import random

word_list = ["wheel","basic","anger","carry","meant","rapid","lower",
                "fight","acute","chase","yield","visit","women","north","chose"]

picked_word = random.choice(word_list)

print("\n",Fore.GREEN+" Green","indicates that the letter is in the","\n"," correct spot!","\n")
print(Fore.YELLOW+" Yellow","indicates that the letter exists in the correct word. (Can show even if you have","\n","already guessed the correct spot)","\n")

print(picked_word,"\n")   #demonstration purposes

def verifychar(guess):
    return guess.isalpha()

def verifylength(guess):     # checks if word is a valid length
    return len(guess) == 5

def compareguess(guess,picked_word):      #will check each letter in the picked word and compare it with the guessed word
    comparedresult = ""

    for i in range(len(guess)):
        if guess[i] == picked_word[i]:
            comparedresult += Fore.GREEN + guess[i]
        else:
            if guess[i] in picked_word:
                comparedresult += Fore.YELLOW + guess[i]
            else:
                comparedresult += Fore.WHITE + guess[i]

    return print(comparedresult)

def guessinggame():
    counter = 0
    maxcounter = 8
    while counter < maxcounter:
        counter += 1
        guess = input("Enter your five-letter guess: ")     #User is prompted

        if verifylength(guess) == True and verifychar(guess) == True:
            if guess == picked_word:
                print("\n",Fore.CYAN+"Correct!","\n","----------------------")
                break
            elif guess != picked_word:
                compareguess(guess,picked_word)
                print()
                continue
                            
        elif verifylength(guess) == False or verifychar(guess) == False:
            print("\n"," Make sure it's five letters or has correct","\n","characters!","\n")
            continue
    if counter == maxcounter and guess != picked_word: 
        print("Nope! The word was",Fore.CYAN + picked_word,"\n","----------------------")

guessinggame()
