from replit import clear
from PIL import Image


# with contextlib.suppress(IOError):
#     img=Image.open(kali3.png)

bids = {}
bidding_finished = False


def find_high_bid(bidding_record):
    highest_bid = 0

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?:")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any more bidders? (y/n):")
    if should_continue == "n":
        bidding_finished = True
        find_high_bid(bids)
        clear()
    elif should_continue == "y":
        clear()




# travel_log = [
#     {"country": "France", "cities": ["Paris", "Lille", "Dijon"], "visits": 12},
#     {"country": "Germany", "cities": ["Berlin", "Munich", " Stuttgart"], "visits": 10},
#     {"country": "Italy", "cities": ["Rome", "Venice", "Sofia"], "visits": 10},
# ]


# def add_new_country(country_visited, times_visited, cities_visited):
#     new_country = {
#         "country": country_visited,
#         "cities": cities_visited,
#         "visited": times_visited,
#     }
#     travel_log.append(new_country)


# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
