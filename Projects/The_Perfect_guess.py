import random

num = random.randint(1,25)
num = str(num)
guess = 1
while (True):
    print("Enter q To Quit")
    play = input("Enter The Number Between 1 to 25 : ")
    if play =='q':
        print("Thanks for playing this game")
        break
    elif play > num :
        guess = guess + 1
        print("Please Enter lower number")
    elif play < num :
        guess = guess + 1
        print("Please Enter higher number")
    elif play == num:
        print(f"You Guessed it right in {guess} guess")
        break
    else:
        print("Try Again")
        guess = guess + 1
