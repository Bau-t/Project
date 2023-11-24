import colorama 
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

import random

word_list = ["wheel","basic","anger","carry","meant","rapid","lower",
                "fight","acute","chase","yield","visit","women","north","chose"]

picked_word = random.choice(word_list)

print("\n",Fore.GREEN+"Green","indicates that the letter is in the","\n"," correct spot!","\n")
print(Fore.YELLOW+" Yellow","indicates that the letter exists in the  correct word. (Can show even if you have","\n"," already guessed the correct spot)","\n")

print(Fore.CYAN + picked_word,"    \033[3mdisplayed for demonstration purposes\033[0m","\n")   #demonstration purposes

def verifychar(guess):          # checks if the characters are valid
    return guess.isalpha()

def verifylength(guess):     # checks if word is a valid length
    return len(guess) == 5

def compareguess(guess,picked_word):      #will check each letter in the picked word and compare it with the guessed word
    comparedresult = ""                   #green will indicate correct spot, yellow will indicate the letter exists in the word but not the correct spot

    for i in range(len(guess)):
        if guess[i] == picked_word[i]:                  #if the letter from guessed word(1st, 2nd, and so on) and the random word(1st,2nd, and so on) match, it will send it back to the empty string as green
            comparedresult += Fore.GREEN + guess[i]
        else:
            if guess[i] in picked_word:                     #if the letter from the guessed word exists in the random word, it will send it back as  yellow
                comparedresult += Fore.YELLOW + guess[i]
            else:
                comparedresult += Fore.WHITE + guess[i]        #if neither cases are true, it will simply send it back as white

    return print(comparedresult)

def guessinggame():                         #the game
    counter = 0
    maxcounter = 8
    while counter < maxcounter:
        counter += 1
        guess = input("Enter your five-letter guess: ")     #User is prompted

        if verifylength(guess) == True and verifychar(guess) == True:       #if the length and characters are valid, it will continue
            if guess == picked_word:                                                    #if the word is correct, it will print a confirmation
                print("\n",Fore.CYAN+"Correct!","\n","----------------------")
                break
            elif guess != picked_word:                                                  #if the word is not correct, it will compare the two words and print the result
                compareguess(guess,picked_word)
                print()
                continue
                            
        elif verifylength(guess) == False or verifychar(guess) == False:                #if either the length or characters are invalid, it will let you know to try again
            print("\n"," Make sure it's five letters or has correct","\n"," characters!","\n")
            continue
    if counter == maxcounter and guess != picked_word:                              #if the maximum amount of tries has been reached, it will print the correct word
        print("Nope! The word was",Fore.CYAN + picked_word,"\n","----------------------")

guessinggame()          #activating the game
