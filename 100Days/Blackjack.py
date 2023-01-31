import random


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return(sum(cards))

# sourcery skip: merge-list-append, move-assign-in-block
user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score =calculate_score(computer_cards)
