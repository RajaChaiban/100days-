import random
from art import logo,vs
from gamed import data
import os

def clear():
  os.system("cls" if os.name == "nt" else "clear")

def get_random_account():
    return random.choice(data)

def display_data(account):
    name= account["name"]
    descrp=account["description"]
    country=account["country"]
    return f"{name}, a {descrp}, from {country}"

def compare(guess,account_a,account_b):
  if account_a > account_b:
      return guess== "a"
  else:
     return guess =="b"
  


print(logo)
score=0
continue_game=True

account_b=get_random_account()

while continue_game:
  account_a= account_b
  account_b = get_random_account()
  if account_a == account_b:
    account_b = get_random_account()

  print(f"Account a: {display_data(account_a)}")
  print(vs)
  print(f"Account b: {display_data(account_b)}")
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  followers_a=account_a["follower_count"]
  followers_b=account_b["follower_count"]

  is_correct=compare(guess,followers_a,followers_b)

  clear()

  if is_correct:
    score += 1
    print(f"You are right. Your score is {score}.")
  else:
    continue_game =False
    print(f"You are wrong. Your score is {score}.")


