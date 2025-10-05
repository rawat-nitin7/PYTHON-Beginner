#Game(rock,paper,siccors) -- rock as r,paper as p, scissors as s

#if person chooses rock -- p(Win)
#                       -- s(lose)

#if person choose p -- s(Win)
#                   -- r(lose)

#if person choose s -- p(win)
#                   -- r(lose)

import random 

while True:
    a=['ROCK','PAPER','SCISSORS']
    print("PRESS 1 FOR ROCK")
    print("PRESS 2 FOR PAPER")
    print("PRESS 3 FOR SCISSORS")
    user_input=int(input("ENTER YOUR CHOICE: "))
    if user_input not in [1,2,3]:
        print("INVALID CHOICE ")
        continue
    user=a[user_input-1]
    com=random.choice(a)
    print("COMPUTER HAS CHOOSEN:",com)
    if(user=='ROCK' and com=='SCISSORS' ):
        print("YOU WON")
    elif(user=='ROCK' and com== 'PAPER' ):
        print("YOU LOSE")
    elif(user=='PAPER' and com=='SCISSORS'):
        print("YOU WON")
    elif(user=='PAPER' and com== 'ROCK' ):
        print("YOU LOSE")
    elif(user=='SCISSORS' and com=='PAPER'):
        print("YOU WON")
    elif(user=='SCISSORS' and com== 'ROCK' ):
        print("YOU LOSE")
    else:
        print("IT'S A DRAW")
    
    n=input("ENTER DO YOU WANT TO Y/N: ").upper()
    if(n!='Y'):
        break
    