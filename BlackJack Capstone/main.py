import random
# from replit import clear
from art import logo

def deal_card():
    """Return a random card from the deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the card"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "Youn went over, You LOSE!!!"
    elif user_score == computer_score:
        return "It's a DRAW!!!"
    elif computer_score == 0:
        return "You loose, the opponent has BLACKJACK!!!"
    elif user_score == 0:
        return "You WIN with a BLACKJACK!!!"
    elif computer_score > 21:
        return "You WIN, opponent went over"
    elif user_score > 21:
        return "You LOSE, you went over"
    elif user_score > computer_score:
        return "You Win!!!"
    else:
        return "You LOSE!!!"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range (2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over :
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards : {user_cards}, current score {user_score}")
        print(f"Computer first card : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else :
            user_should_deal = input ("'y' for another card, 'n' to pass = ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else :
                is_game_over = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final card in hand {user_cards}, your score {user_score}")
    print(f"computer final card in hand {computer_cards}, and it score {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you wanna play 'y' or not 'n' = ") == "y" :
    # clear()
    play_game()