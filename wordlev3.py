import colorama 
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

import random

word_list = ["wheel","basic","anger","carry","meant","rapid","lower",
             "fight","acute","chase","yield","visit","women","north","chose"]

picked_word = random.choice(word_list)
print("\n",Fore.GREEN+" Green","indicates that the letter is in the","\n"," correct word!","\n")
print(picked_word,"\n")

def verifylength(guess):     # checks if word is a valid length
    return len(guess) == 5

def compareguess(guess):      #will check each letter in the picked word and compare it with the guessed word
   
   for i in guess:
       if i in picked_word:
           i = Fore.GREEN + i
           print(i,end="")

def guessinggame():
    counter = 0
    maxcounter = 5
    while counter < maxcounter:
        counter += 1
        guess = input("Enter your five-letter guess: ")     #User is prompted

        if verifylength(guess) == True:
            if guess == picked_word:
                print("\n",Fore.CYAN+"Correct!","\n","----------------------")
                break
            elif guess != picked_word:
                compareguess(guess)
                print()
                continue
                            
        elif verifylength(guess) == False:
            print("Make sure it's five letters!")
            continue
    if counter == maxcounter and guess != picked_word: 
        print("Nope! The word was",Fore.CYAN + picked_word,"\n","----------------------")

guessinggame()
