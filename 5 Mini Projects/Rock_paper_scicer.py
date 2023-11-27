import random

a = random.randint(1,3)


if a == 1:
    com = "Rock"
elif a == 2:
    com = "Paper"
elif a == 3:
    com = "Scissor"

print("Enter r for Rock p for Paper s for Scissor")
play = input("What you want to choose : ")

print(f"Computer Choose {com}")
if play == 'r':
    if com == "Rock":
        print("Game Draw")
    elif com == "Paper":
        print("You Lose")
    elif com == "Scissor":
        print("You Won")
if play == 'p':
    if com == "Rock":
        print("You Won")
    elif com == "Paper":
        print("Game Draw")
    elif com == "Scissor":
        print("You Lose")
if play == 's':
    if com == "Rock":
        print("You Lose")
    elif com == "Paper":
        print("You Win")
    elif com == "Scissor":
        print("Game Draw")
