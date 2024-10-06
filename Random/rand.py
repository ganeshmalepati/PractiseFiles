from random import randint

min_number = int(input("Enter the min Number: "))
max_number = int(input("Enter the max Number: "))

if(max_number < min_number):
	print("Invalid Input - Shutting Down...")
else:
	rnd_number = randint(min_number, max_number)
	print(rnd_number)