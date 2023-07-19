import random
list=["Rock","Paper","Scissors"]
user=int(input("Pick a number.Type 0 for Rock,1 for Paper and 2 for Scissors\n"))
bot=random.randint(0,2)
 
print("You have selected: "+ list[user])
print("The computer selected: "+ list[bot])

if user>=3 and user<0:
    print("You typed an invalid number")
elif user==2 and bot==0:
    print("You have Lost!")
elif user==0 and bot==2:
    print("You have Won!")
elif user > bot:
    print("You have Won!")
elif bot > user:
    print("You have Lost!")

elif user==bot:
    print("It's a draw!")
else :
    print("You typed an invalid number")

