import random

def pc():
    num = random.randint(1, 3)
    if num == 1:
        return "rock"
    elif num == 2:
        return "paper"
    elif num == 3:
        return "scissors"

def result():
    u_input = input("Enter 'rock', 'paper', or 'scissors': ").lower()
    comp = pc()
    
    if u_input == "rock" and comp == "scissors":
        print("Computer chose scissors, you win!")
    elif u_input == "rock" and comp == "paper":
        print("Computer chose paper, you lose.")
    elif u_input == "rock" and comp == "rock":
        print("Computer chose rock, it's a tie.")
    elif u_input == "paper" and comp == "scissors":
        print("Computer chose scissors, you lose.")
    elif u_input == "paper" and comp == "paper":
        print("Computer chose paper, it's a tie.")
    elif u_input == "paper" and comp == "rock":
        print("Computer chose rock, you win!")
    elif u_input == "scissors" and comp == "scissors":
        print("Computer chose scissors, it's a tie.")
    elif u_input == "scissors" and comp == "paper":
        print("Computer chose paper, you win!")
    elif u_input == "scissors" and comp == "rock":
        print("Computer chose rock, you lose.")
    else:
        print("Invalid input.")

while True:
    result()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
