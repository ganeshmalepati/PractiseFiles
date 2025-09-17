import random
def RollingDice():
    roll_dice_again = "Y"
    while roll_dice_again == "Y":
        A = random.randint(1, 6)
        B = random.randint(1, 6)
        print(f"Dice 1: {A} \nDice 2: {B} ")
        if A == B:
            print("Both dices have same face value")
        roll_dice_again = input("Roll the dice again?: {Y/N} ")
RollingDice()
