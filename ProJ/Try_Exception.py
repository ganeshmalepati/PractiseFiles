# try and exeception handling in python
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter b number: "))
    c = a/b
    d = a * b
    print(c)
    print(d)
except ZeroDivisionError:
    print("The Error Occurred here is a Zero divison error")
except ArithmeticError:
    print("In this the arthemetic operator is not working")
except ValueError:
    print("Please enter numbers not string and other types")
except TypeError:
    print("Please enter correct type of value")

print("Hey, your handling your own exceptions")


