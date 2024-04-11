import random

print("Welcome to Coin Fliper by ShivanshuWeb")

heads = 0
tails = 0
counts = 0
l1 = ['Heads','Tails']
while True:
    user = input("Enter f to Flip the coin (q to quit) : ")
    if user == 'f':
        rand =  random.choice(l1)
        if rand == 'Heads':
            print("You got Heads")
            heads = heads + 1 
            print(f"Total Heads : {heads} Total Tails : {tails}")
        else:
            print("You got Tails")
            tails = tails + 1 
            print(f"Total Heads : {heads} Total Tails : {tails}")
        counts = counts + 1
    elif user == 'q':
        print(f"Total Heads : {heads}\nTotal Tails : {tails}\nNo. of Counts : {counts}")
        break
    else:
        print("Try again...")