import random
def PasswordGenerator(num_letters, num_number, num_symbols):
    letters = "abcdefghilmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    symbols = "@#$&*_"
    password = random.choices(letters, k = num_letters) + random.choices(numbers, k = num_number) + random.choices(symbols, k = num_symbols)
    random.shuffle(password)
    Entire_password = ''.join(password)
    return Entire_password


num_letters = int(input("How many letters do you want in your password? "))
num_number = int(input("How many numbers do you want in your password? "))
num_symbols = int(input("How many symbols do you want in your password? "))
a = PasswordGenerator(num_letters, num_number, num_symbols)
print(f"Your password is {a}")
