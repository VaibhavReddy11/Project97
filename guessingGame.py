import random

number = random.randint(1, 9)

chances = 1
guess = input("Enter Your Guess")

while chances < 5:
    if guess == number:
        print("Congratulation YOU WON!!!")
        break
    else:
        chances = chances + 1
        guess = input("Guess again")

if not chances < 5:
    print("YOU LOSE!!! The number is", number)