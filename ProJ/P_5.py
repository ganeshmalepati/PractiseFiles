def ScoreChecker(score):
    if score >= 0.0 and score <= 1.0:
        if score >= 0.9:
            print("Your Grade is A")
        elif score >= 0.8:
            print("Your Grade is B")
        elif score >= 0.7:
            print("Your Grade is C")
        elif score <= 0.6:
            print("You have failed your exam")
    else:
        print("Bad Score")
score = float(input("Enter your Grade: "))
ScoreChecker(score)