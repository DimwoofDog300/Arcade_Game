import random

def user_hangman_input():
    while True:
        try:
            user_hangman_input = int(input("Welcome to hangman, choose a theme. Input either 'fruits' or 'hangman'")).lower()
            print("You have chosen to play {user_hangman_input}")
        except ValueError:
            user_hangman_input = int(input("Welcome to hangman, choose a theme. Input either 'fruits' or 'hangman'")).lower()
    fruits = ['apple', 'watermelon', 'mango']
    weapons = ['flamethrower', 'assult rifle', 'bow']
    if user_hangman_word == fruits:
        pick_fruits = random.choice(fruits)
        return pick_fruits
    else user_hangman_word == weapons:
        pick_weapons = random.choice(weapons)
        return pick_weapons

