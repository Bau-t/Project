import random 

wordlist = ["wheel","basic","anger","carry","meant","rapid","lower","fight","acute","chase","yield","visit","women","north","chose"]
picked_word = random.choice(wordlist)
guess = input("We have chosen a five letter word. Enter your guess here: ")

guess_count = 0
while guess_count < 5:
    if guess == picked_word:
        print("Correct",guess,"is correct!")
    elif guess != picked_word:
        print("Nice guess, but that is not correct. Try again.")
        guess_count += 1
