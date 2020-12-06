from art import logo
from random import randint

easy_level_turn = 10
hard_level_turn = 5

def compare(guess, number, live):
    """coparing guess with the number and count the life"""
    if guess < number:
        print("its LOWER from the number")
        return live - 1
    elif guess > number:
        print("its HIGHER from the number")
        return live - 1
    else :
        print(f"you right {guess} is the number")

def set_difficulty():
    level = input("Select your difficulty 'easy' or 'hard = ")
    if level == "easy":
        return easy_level_turn
    else:
        return hard_level_turn

def game() :
    print(logo)
    game_finished = False

    print("Welcome to the game")
    print("I've chosen one number from 1 to 100")
    answer = randint(1, 100)
    print(f"hint = {answer}")

    turns = set_difficulty()
    guess = 0
    while guess != answer :
        print(f"you have {turns} to guessing the number")

        guess = int(input("Enter your guess = "))

        turns = compare(guess, answer, turns)
        if turns == 0:
            print("You run out attemp you LOSE")
            return
        elif guess != answer:
            print("guess again")

game()


