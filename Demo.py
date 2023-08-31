#display the two choices
from gamed import data
import os
def clear():
  os.system("cls" if os.name == "nt" else "clear")

import random
from art import logo, vs

def get_random_account():
    return random.choice(data)

def format_data(account):
    account_name= account["name"]
    account_discrp= account["description"]
    account_country= account["country"]
    return (f"{account_name}, a {account_discrp}, from {account_country}")

def check_answer(guess,a_followers,b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score=0
game_continue=True

account_b = get_random_account()

while game_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
        account_b = get_random_account()

    print(f"Account A: {format_data(account_a)}")
    print (vs)
    print(f"Against Account B: {format_data(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_account=account_a["follower_count"]
    b_follower_account=account_b["follower_count"]
    is_correct= check_answer(guess,a_follower_account,b_follower_account)
    
    clear()
    if is_correct:
        
        score+=1
        print(f"You've got the right answer! Current score: {score} ")   
        
    else:
        game_continue=False
        print(f"Sorry that is wrong. Final score: {score}")

