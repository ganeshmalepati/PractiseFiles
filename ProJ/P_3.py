import random
def GuessNumber():
    num  = random.randint(1, 100)
    a = -1
    guess = 0
    while(a != num):
        guess += 1
        a = int(input("Guess the Number: "))
        if a > num :
            print("Lower Number Please")
        else:
            print("Higher number please")
    print(f"You have guessed the correct number after {guess} attemnts")
GuessNumber()
# print(f"You have guessed the correct number {a}")