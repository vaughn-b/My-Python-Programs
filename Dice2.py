# Name:             Instructor
# Course/Section:   ITP100-0? (W or H)
# Assignment:       Exercise: 07
# Program:          Dice02xx.py
#--------------------------------------------------------------

import random

def get_bet(bank):
    bet = -1
    while bet > bank or bet < 0:
        try:
            bet=int(input("Enter your bet => "))
        except ValueError:
            bet = -1
    return bet

def get_guess():
    guess=0
    while (guess < 2 or guess > 12):
        try:
            guess=int(input("Chose a number between 2 and 12: "))
        except ValueError:
            guess = 0
    return guess

def rollDice(x):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    x = int(die1 + die2)
    return x

def prog_info():
    print("My Dice Game .v02")
    print("You have three rolls of the dice to match a number you select.")
    print("Good Luck!!")
    print("---------------------------------------------------------------")
    print("You will win 2 times your wager if you guess on the 1st Roll")
    print("You will win 1 1/2 times your wager if you guess on the 2nd Roll")
    print("You can win your wager if you guess on the 3rd Roll")
    print("---------------------------------------------------------------")

prog_info()
bank = 500
print("You have $",bank,"in your bank")
bet = get_bet(bank)
x = 0
while bank > 0 and bet != 0:
    guess = get_guess()
    count=1
    while count < 4:
        roll=rollDice(x)
        print("Die Roll #",count,"was ",roll)
        if roll==guess:
            if count == 1:
                bank = bank+(bet*2)
            elif count== 2:
                bank=bank+(bet*1.5)
            else:
                bank=bank+bet
            count = 4
        elif count == 3:
            bank=bank-bet
        count = count+1
    if bank != 0:
        print("You have $",bank,"in your bank")
        bet = get_bet(bank)
print("You have $",bank,"left in your bank")
print("Thanks for playing")



    
