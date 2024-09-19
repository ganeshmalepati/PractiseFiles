
def Occurence(str):
    Each_char = {}
    for i in str:
        if i in Each_char:
            Each_char[i] += 1
        else:
            Each_char[i] = 1
    print(f"The occurence of each character in the given string is :\n  {Each_char}")
str = input("Enter your String: ")
Occurence(str)
