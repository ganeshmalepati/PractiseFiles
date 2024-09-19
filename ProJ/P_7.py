def Max_of_three_num(a, b, c):
    if a>b and a>c:
        return f"{a} is the greater number among the given number"
    elif b>a and b>c:
        return f"{b} is the greater number among the given number"
    else:
        return f"{c} is the greater number among the given number"
a =int(input("Enter the a value: "))
b =int(input("Enter the b value: "))
c =int(input("Enter the c value: "))
print(Max_of_three_num(a, b, c))