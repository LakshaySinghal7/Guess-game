import random

num_range=input("Enter a number upto which you wanna make guesses: ")

if num_range.isdigit():
    toprange= int(num_range)
else:
    print("Next use your brain enter a 'NUMBER'")
    quit()

randomnum= random.randint(0,toprange)

guesses=0
flag= False
while guesses<=10:
    guesses+=1
    answer=input("Guess the number now: ")
    if answer.isdigit():
        usergues=int(answer)
    else:
        print("Please enter a number next Time!")
        continue
    if usergues==randomnum:
        print("Wohoo You Got it")
        flag= True
        break
    elif usergues>randomnum:
        print("You entered above")
    else:
        print("You entered below")
if flag:
    print("You guessed in", guesses, "guesses")
else:
    print("Turns exhausted the number was:", randomnum)