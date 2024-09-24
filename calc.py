import random

def pc():
    num = random.randint(1,3)
    if num == 1:
        return "rock"
    elif num == 2:
        return "paper"
    elif num == 3:
        return "scissors"

u_input = input("Enter 'rock' 'paper' or 'scissors'")


def result():
    comp = pc()
    if u_input == "rock" and comp == "scissors":
        print("computer chose scissors u win")
    elif u_input == "rock" and comp == "paper":
        print("computer chose paper u lose")
    elif u_input == "rock" and comp == "rock":
        print("computer chose rock its a tie")
    elif u_input == "paper" and comp == "scissors":
        print("computer chose scissors u lose")
    elif u_input == "paper" and comp == "paper":
        print("computer chose paper its a tie")
    elif u_input == "paper" and comp == "rock":
        print("computer chose rock u win")
    elif u_input == "scissors" and comp == "scissors":
        print("computer chose scissors its a tie")
    elif u_input == "scissors" and comp == "paper":
        print("computer chose paper u win")
    elif u_input == "scissors" and comp == "rock":
        print("computer chose rock its u lose")
    else:
        print("ur retarded")
result()
