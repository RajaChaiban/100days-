#function difficulty
#input difficuly
#link easy to 5 and hard to 10
#user guesses
#function that has number and guess(if statement)
#track number of turns and reduce by 1

import random

def difficulty(level):
    if level== 'hard':
        return 5
    elif level == 'easy':
        return 10
    else:
        print("Please enter a new number")

def check_answer(answer,guess,turns):
    if guess > answer:
        print("Too High")
        return turns-1
    elif guess < answer:
        print("Too Low")
        return turns-1
    else:
        print(f"You've got the answer {answer}")

def game():

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer= random.randint(1,100)
    level=input("Choose a difficulty: 'easy' or 'hard' ")
    print(f"Pssst, the correct answer is {answer}") 
    turns=difficulty(level)

    guess=0

    while guess!= answer:
        print(f"You have {turns} chances left")
        guess=int(input("Please Enter a number: "))
        turns=check_answer(answer,guess,turns)
        if turns==0:
            print("You have ran out of chances")
            return
        elif guess!= answer:
            print("Guess another number")

game()