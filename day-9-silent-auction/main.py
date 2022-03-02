from replit import clear
import art

print(art.logo)
print("Welcome to the secret auction program.")

bidders = []

def add_bidders(name, bid):
    bidding = {}
    bidding['name'] = name
    bidding['bid'] = bid

    bidders.append(bidding)

def get_winning_bid():
    max_bid = 0
    max_bidder = ""
    for bidder in bidders :
        if bidder['bid'] > max_bid:
            max_bid = bidder['bid']
            max_bidder = bidder['name']

    print(f"The winner is {max_bidder} with a bid of ${max_bid}")
        

answer = 'yes'
while answer == 'yes' or answer == 'y':
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    add_bidders(name, bid)

    answer = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    clear()

get_winning_bid()

