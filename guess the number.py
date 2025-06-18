import random

num = random.randint(0,100)

print("Guess the number from 0 - 100!")

numofguess = 0

while True: 
    try:
        guessed = int(input())
    except ValueError:
        print("Please type a valid number")
        continue

    if guessed == num:
        numofguess += 1
        print(f"Good job! You guessed {numofguess} times! Guess anyone can figure it out with that many clues huh. :P")
        break
    elif abs(guessed - num) <= 10:
        if guessed > num:
            numofguess += 1
            print("Ohhh, close but still too big")
        elif guessed < num:
            numofguess += 1
            print("Super close! try adding a bit more") 
    elif guessed > num:
            numofguess += 1
            print("Too big")
    elif guessed < num:
            numofguess += 1
            print("Too smalll")             


