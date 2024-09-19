def Temperature(temp):
    if temp > 28:
        return "hot"
    elif temp > 18 and temp < 28:
        return "warm"
    else:
        return "cold"
temp = int(input("Enter temperature value: "))
print(Temperature(temp))