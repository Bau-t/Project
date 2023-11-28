import random 

wordlist = ["wheel","basic","anger","carry","meant","rapid","lower","fight","acute","chase","yield","visit","women","north","chose"]
guess = input("We have chosen a five letter word. Enter your guess here: ")
guess_count = 0
picked_word = random.choice(wordlist)

while guess_count < 5:
    if guess == picked_word:
        print("Correct",guess,"is correct!")
    else:
        print("Nice guess, but that is not correct. Try again.")
        guess = input("We have chosen a five letter word. Enter your guess here: ")
    guess_count += 1
