import os
def clear():
  os.system("cls" if os.name == "nt" else "clear")

bids = {}

highest_bid=0
def find_highest_bidder(bidding_record):
    winner=""
    for bidder in bidding_record:
       bid_amount= bidding_record[bidder]
       if bid_amount> highest_bid:
           highest_bid = bid_amount
           winner = bidder
    print(f"The winnner is {winner} with a bid of ${highest_bid}")

bid=True
while not bid:
  name= input("What is your Name: ")
  price= input ("What is your Bid? $")
  bids[name]=price
  bid_again=input("Are there any other bidders? 'yes'or 'no' ").lower()
  if bid_again=='no':
    bid=False
    find_highest_bidder(bidder=name,bid_amount=price)
  elif bid_again =='yes':
    clear()