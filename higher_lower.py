from game_data import data
from art import logo, vs
import random
import os

def clear():
    os.system("clear")


def format_account_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, count1, count2):
    """Take the user guess and follower counts na return if they got it right."""
    if count1 > count2:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
current_score = 0
game_should_continue = True
selected2 = random.choice(data)

while game_should_continue:
    # Randomly select a person1 from game_date 
    selected1 = selected2
    selected2 = random.choice(data)
    
    while selected1 == selected2:
        selected2 = random.choice(data)

    # Display name and other details of selected people
    print(f"Compare A: {format_account_data(selected1)}.")
    print(vs)
    print(f"Against B: {format_account_data(selected2)}.")

    # Ask the user to choose A or B, indicating who has more IG followers
    answer = input("Who has more Instagram followers? Type 'A' or 'B': ").lower()

    # Set the logic for deciding the whether the answer is correct or false
    follower_count1 = selected1["follower_count"]                                   
    follower_count2 = selected2["follower_count"]
    is_correct = check_answer(answer, follower_count1, follower_count2)
    
    clear()
    print(logo)

    if is_correct:
        current_score += 1
        print(f"You are right. Current score: {current_score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {current_score}.")
