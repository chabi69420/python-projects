
import random

print("Welcome to the Dice Roller!")

while True:
    input("Press Enter to roll the dice...")
    dice = random.randint(1, 6)
    print("You rolled a", dice)

    choice = input("Roll again? (yes/no): ")
    if choice.lower() != "yes":
        print("Thanks for playing!")
        break
