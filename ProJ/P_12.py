import random
def RockPaperScissor():
    while True: 
        user_action = input("Enter your choice(Rock, Paper, Scissor): ")
        select_choice = ["Rock", "Paper", "Scissor"]
        computer_action = random.choice(select_choice)
        print(f"You choice is {user_action} and Computer Choice is {computer_action}")
        if user_action == computer_action:
            print(f"Both players selected a {user_action}. It's a Tie")
        elif user_action == "Rock":
            if computer_action == "Scissor":
                print("Rock smashes the scissor. You won")
            else:
                print("Paper Covers the rock. You lose")
        elif user_action == "Paper":
            if computer_action == "Scissor":
                print("Scissore cuts the paper. You Lose")
            else:
                print("Paper covers rock. You won")
        elif user_action == "Scissor":
            if computer_action == "Paper":
                print("Scissore cuts the paper. You Won")
            else:
                print("Rock smashes the scissor. You Lose")
        play_again = input("Choose whether to play again or not (Y/N): ")
        if play_again != "Y":
            break

RockPaperScissor()