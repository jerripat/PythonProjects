import random
from tkinter import *
from tkinter import messagebox
from replit import clear
from PIL import Image, ImageTk

tk = Tk()
result = ''
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw "
    elif c_score == 0:
        return "Lose"
    elif u_score == 0:
        return "Win with a Blackjack "
    elif u_score > 21:
        return "You went over "
    elif c_score > 21:
        return "Opponent went over! You win "
    elif u_score > c_score:
        return "You win "
    else:
        return "You Lose!"

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

img = ImageTk.PhotoImage(Image.open("Poker-icon.png"))
img_label = Label(tk, image=img)
img_label.pack()


result =input("Would you like to play a game? (y/n): ")
if result == "y":
    play_game()
    user_cards = []
    computer_cards = []
    is_game_over = False

def replay_game():
    if result == "y":
        ans = input('Play another game?')
        clear()
        if ans == "y":
            play_game()
    else:
        print('Okay...Goodbye')
        exit()
    # sourcery skip: merge-list-append, move-assign-in-block

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f" Your cards: {user_cards}, current_score: {user_score}")
    print(f" Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to draw another card, or 'n' to pass: ")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True
clear()
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(f"  Your final hand {user_cards}, final score: {user_score}")
print(f"  Computers final hand: {computer_cards}, final score: {computer_score}")
print(compare(user_score, computer_score))
replay_game()

mainloop()
