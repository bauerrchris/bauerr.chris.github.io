#!/usr/bin/env python
# coding: utf-8

# In[32]:


cash=250
game=1
con=0
import random
while game==1:
    print("Hello! Welcome to the dice game.")
    print("There are some very simple rules I need you to understand:")
    print("-You start with $250. Each time you bet x amount of money before you roll the dice.")
    print("-The dice are then rolled and you guess if your next roll be higher or lower.")
    print("-If you guessed right, you win twice the amount you bet.")
    print("-But, if you guess wrong, you lose the amount you bet. The game continues until you lose all your money or decide to quit.")
    print("-Here are some technicalities you should know. If the sum of the first roll and the second are the same, you lose.")
    game=game+1
    start=float(input(print("Enter 1 to continue")))
    while start==1:
        start=start+1
        print("You have $: ",cash)
        con=float(input(print("Enter 1 to Continue")))
        while con==1:       
            bet=float(input(print("How much would you like to bet?")))
            if cash-bet<0:
                print("You do not have enough cash to bet that amount. Try a different amount. Your remaining amount: ",cash)
                con=1
            elif cash-bet>=0:
                print("Your bet is: ",bet)
                con=con+1
            else:
                print("You must bet at least 1.")
                con=1

            co=1
        while co==1:
            for i in range(1):
                di1=random.randint(1,6)
                di2=random.randint(1,6)
                co=co+1
                pctot=di1+di2
                print(di1)
                print(di2)
                print("The pc rolled: ",di1,"+",di2,"=",pctot)

            c=1
        while c==1:
            guess=input(print("Do you think that your next number will be higher or lower?"))
            if guess=="higher":
                c=c+1
            elif guess=="lower":
                c=c+1
            else:
                print("That is neither higher nor lower")
                c=c
            print("You guessed: ",guess)
            gues=input(print("Is this correct? Y/N"))
            if gues=="Y":
                c=c+1
            elif gues=="N":
                c=c
            else:
                print("That wasn't Y or N.")
                c=c

            cont=1
        while cont==1:
            for o in range(1):
                di3=random.randint(1,6)
                di4=random.randint(1,6)
                cont=cont+1
                ustot=di3+di4
                print(di3)
                print(di4)
                print("You rolled: ",di3,"+",di4,"=",ustot)

            wl=1
        while wl==1:
            if  pctot==ustot:
                print("You lost: ",bet)
                cash=cash-bet
                wl=wl+1
            elif (pctot<ustot and guess=="higher"):
                print("You have won!")
                cash=cash+bet+bet
                wl=wl+1
            elif (pctot<ustot and guess=="lower"):
                print("You have lost :/")
                cash=cash-bet
                wl=wl+1
            elif (pctot>ustot and guess=="lower"):
                print("You have won!")
                cash=cash+bet+bet
                wl=wl+1
            elif(pctot>ustot and guess=="higher"):
                print("You have lost :/")
                cash=cash-bet
                wl=wl+1
        if cash==0:
            print("You are out of money and have lost.")
        else:                          
            again=input(print("Would you like to play again? Y/y/N/n"))
            if again=="Y":
                start=start-1
            elif again=="y":
                start=start-1
            elif again=="N":
                start=start
            elif again=="n":    
                start=start
            else:
                print("That was not a correct input. Try Y/y/N/n")
print("Thank you for playing this game.")

    
    

