import random

a = random.randint(1,6)
roll = input("Enter R to Roll The Dice : ")
    
if roll == 'r' or roll == 'R':
    print(f"You Got {a} By Rolling The Dice")

else:
    print("Try Again")