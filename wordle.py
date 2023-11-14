import random 

wordlist = ["wheel","basic","anger","carry","meant","rapid","lower","fight","acute","chase","yield","visit","women","north","chose"]
picked_word = random.choice(wordlist)
guess = input("We have chosen a five letter word. Enter your guess here: ")

guess_count = 0
while guess_count < 5:
    if guess == picked_word:
        print("You are correct!")
    elif guess != picked_word:
        print("Incorrect!")
        guess_count += 1
