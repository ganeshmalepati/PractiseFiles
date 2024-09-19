# def FizzBuzz():
#     for num in range(1, 100):
#         if num % 5 == 0 and num % 7 == 0:
#             print("FizzBuzz")
#         elif num % 7 == 0:
#             print("Buzz")
#         elif num % 5 == 0:
#             print("Fizz")
#         else:
#             print(num)

# FizzBuzz()

import random

def GuessingANumber():
    num = random.randint(1, 100)
    a = - 1
    count = 0
    while a != num:
        count += 1
        a = int(input("Enter a Number: "))
        if a > num:
            print("Your Guess number is to high")
        elif a < num:
            print("Your Guess number is too low")
        else:
            print(f"You have guessed the correct number after {count} counts")

GuessingANumber()