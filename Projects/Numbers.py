import random

d = 1
a = random.randint(0, 20)       # Randint function of random helps to chose a random number
a = str(a)                      # To convert int of a to str

while (True):
    print("Enter Q to Quit")                                 # break the while loop
    num = input("Enter the number between 1 to 20 : ")       # takes input in str form
    if num == 'q':                                           # if entered q then the program breaks
        print("Thanks For Playing")
        break     
    elif num == a :                                          # if entered right then program tells entered right statement
        print(f"You Entered it Right in {d} Try")

    elif d == 10:
        print("You Loss the game You have try 10 times")
    elif num > a :
        print("Enter Smaller Number")
        d = d + 1
    elif num < a :
        print("Enter Greater Number")
        d = d + 1
    