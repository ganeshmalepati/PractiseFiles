def GrossPay(hours, rate):
    try:
        hours = float(input("Enter hours: "))
    except ValueError:
        return "Error!, Please enter numeric input for hour"
        quit()
    try:
        rate = float(input("Enter rate: "))
    except ValueError:
        return "Error!, Please enter numeric input for rate"
        quit()

    if hours < 40:
        return round(hours * rate, 2)
    else:
        overtime = hours - 40
        return round(40 * rate + overtime * rate * 1.5, 2)
    
hours = 3
rate = 5
print(GrossPay(hours, rate))
