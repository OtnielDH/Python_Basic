import random
from random import randint
from game_data import data
from art import logo, vs

def get_random():
    """get random data"""
    return random.choice(data)

def format_data(account):
    """print the data out"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name} a {description} from {country}"

def check_follower(guess, follower_a, follower_b):
    if follower_a > follower_b:
        return guess == "a"
    else:
        return guess == "b"
def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random()
    account_b = get_random()

    while game_should_continue:
        account_a = account_b
        account_b = get_random()

        if account_a == account_b :
            account_b = get_random()
        
        print(f"Compare {format_data(account_a)}")
        print(vs)
        print(f"Againts {format_data(account_b)}")

        guess = input("Guess who is higher 'A' or 'B' = ").lower()
        a_follower_account = account_a["follower_count"]
        b_follower_account = account_b["follower_count"]
        is_correct = check_follower(guess, a_follower_account, b_follower_account)

        print(logo)
        if is_correct:
            score += 1
            print(f"you right your score is {score}")
        else:
            game_should_continue = False
            print(f"Sorry you wrong, final score is {score}")

game()