import random
import os
def clear():
  os.system("cls" if os.name == "nt" else "clear")

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    if len(cards)==2 and sum(cards)==21:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_cards(user_score,computer_score):
    if user_score>21 and computer_score>21:
        return "You went over, You Lose"
    if user_score== computer_score:
        return "Draw"
    elif computer_score== 0:
        return "You Lose"
    elif user_score ==0:
        return "BlackJack"
    elif user_score >21:
        return "Went Over 21, You Lose"
    elif computer_score>21:
        return "Went Over 21, You Win"
    elif user_score > computer_score:
        return "You Win"
    else: 
        return "You Lose"

def play_blackjack():
    end_game= False
    user_cards=[]
    computer_cards=[]

    for x in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
      
    while not end_game:
        user_score= calculate_score(user_cards)
        computer_score= calculate_score(computer_cards)
        print(f" User Cards: {user_cards}, Score: {user_score}")
        print(f" Computer Cards: {computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            end_game=True
        else:
            user_should_deal=input("Type 'y' to get another card, Type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                end_game=True

    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
        
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand:{computer_cards},final score: {computer_score}")
    print(compare_cards(user_score,computer_score))

while input("Do you want to play the game of blackjack: Type 'y' or 'n': ") == 'y':
    clear()
    play_blackjack()