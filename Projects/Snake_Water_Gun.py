import random

a = random.randint(1,3)


if a == 1:
    com = "Snake"
elif a == 2:
    com = "Water"
elif a == 3:
    com = "Gun"

print("Enter s for Snake w for Water g for Gun")
play = input("What you want to choose : ")

print(f"Computer Choose {com}")
if play == 's':
    if com == "Snake":
        print("Game Draw")
    elif com == "Water":
        print("You Won")
    elif com == "Gun":
        print("You Lose")
if play == 'w':
    if com == "Snake":
        print("You Lose")
    elif com == "Water":
        print("Game Draw")
    elif com == "Gun":
        print("You Won")
if play == 'g':
    if com == "Snake":
        print("You Won")
    elif com == "Water":
        print("You Lose")
    elif com == "Gun":
        print("Game Draw")