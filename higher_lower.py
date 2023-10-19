from game_data import data
from art import logo, vs
import random

# Randomly select a person1 from game_date 
max = len(data)
selected1 = random.randint(0, max)
selected_person1 = data[selected1]

# Randomly select a person2 from game_date 
selected2 = random.randint(0, max)
selected_person2 = data[selected2]

# Display name and other details of selected people with VS
name1 = selected_person1["name"]
description1 = selected_person1["description"]
country1 = selected_person1["country"]

name2 = selected_person2["name"]
description2 = selected_person2["description"]
country2 = selected_person2["country"]

print(f"Compare A: {name1}, a {description1}, from {country1}.")
print(vs)
print(f"Compare A: {name2}, a {description2}, from {country2}.")

# Ask the user to choose A or B, indicating who has more IG followers
answer = input("Who has more Instagram followers? Type 'A' or 'B': ")