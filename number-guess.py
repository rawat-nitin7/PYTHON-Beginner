# Number Guessing Game

# 🧠 The program randomly selects a number, and the user has to guess it.
# Concepts used: loops, conditionals, random numbers.
# Libraries: random
# Example: “I’m thinking of a number between 1 and 100 — can you guess it?”

import random

while True:
    print("GUESS THE NUMBER BETWEEN 1-100")
    print("YOU WILL GET 5 CHANCHES TO GUESS THE NUMBER")
    number=random.randint(0,100)
    c=5
    for i in range (0,5):
        try:
            user_input=int(input("ENTER THE NUMBER: "))
        except ValueError:
            print("INVALID INPUT!!!!! ENTER THE VALID NUMBER")
            continue
        if(user_input>100):
            print("ENTER THE VALUE BETWEEN 1-100")
            continue
        c-=1
        if(user_input==number):
            print("YOU GUESSED THE NUMBER")
            break
        elif(c==0):
            print("OUT OF CHANCES TO GUESS THE NUMBER")
        elif(user_input!=number):
            print("TRY AGAIN")
    user=input('''TO EXIT PRESS N/n:
TO CONTINUE PRESS ANY KEY''').lower()
    if(user=='n'):
        print("YOU HAVE EXITED THE GAME")
        break
    elif(user!='n'):
        print("YOU CAN CONTINUE THE GAME")

        

