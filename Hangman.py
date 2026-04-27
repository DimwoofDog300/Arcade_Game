import random
import time

best_scores_hangman = []
fruits = ['apple', 'watermelon', 'mango', 'strawberry', 'blueberry', 'orange', 'durian', 'lychee', 'jackfruit']
weapons = ['flamethrower', 'assault rifle', 'bow', 'crossbow', 'minigun', 'knife', 'katana']

def get_word_hangman(): # function that gets a word based on users entered theme
    while True:
        theme = input("Welcome to hangman, choose a theme. Input either 'fruits' or 'weapons'").lower().strip() # Asks input for a theme
        if theme == 'fruits':
            pick_fruits = random.choice(fruits) # chooses a random word from the fruits list
            return pick_fruits
        elif theme == 'weapons':
            pick_weapons = random.choice(weapons)
            return pick_weapons # chooses a random word from the weapons list
        else:
            print("Invalid input, either input 'fruits' or 'weapons'")

def show_scores_hangman(): # function that displays score
    if len(best_scores_hangman) > 0: # if list is has 1 or more items
        print('HANGMAN SCORES LEADERBOARD:')
        for i, score in enumerate(best_scores_hangman, 1): # pairs each item in a list with its index
            print(f"{i}. {score} wrong guesses") # prints its place and the corresponding value
    else: # if it has no items
        print("No hangman scores yet.")
        print('')

def play_hangman(): # Function to play the game
    word_hangman = get_word_hangman() # calls the function to get a word
    guessed_letters = [] # makes a empty list
    wrong_guesses = 0 # Sets your guesses to 0
    max_wrong = 6 # Sets a boundry on how many incorrect answers you allowed to have

    global best_scores_hangman # allows this variable to be used inside this function

    print('This game you are given 6 chances to guess a completely unknown word only given a theme')
    time.sleep(1)
    print('You need to enter a letter and if it is in the word it will show where it is, uses this to guess the word')

    time.sleep(1)

    print(f"The word is {len(word_hangman)} letters long and you have 6 guesses") # lists the length of the word you need to guess

    while wrong_guesses < max_wrong: #while loop that works when you
        for letter in word_hangman: # For each letter in the word chosen
            if letter in guessed_letters:  # If the letter has been guessed before
                print(letter, end=' ')  #print the actual letter with a space after it
            else:
                print('_', end=' ')  # prints a blank with a space after it

        if guessed_letters: # shows all letters already used
            print("Guessed letters:", ', '.join(guessed_letters))
        else: # shows there is no guessed letters yet
            print("Guessed letters: None")

        print(f'Guesses remaining: {max_wrong - wrong_guesses}') # shows the amount of guesses left


        guess = input('Guess a letter: ').lower().strip() # asks user to guess a letter

        if len(guess) == 0:  # If the user entered nothing
            print("You didn't enter anything.")
            continue

        if len(guess) != 1 or not guess.isalpha():  # If it is more than 1 character or not a letter
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters: # if letter is already guessed
            print(f"You have already guessed '{guess}', try another.")
            continue


        guessed_letters.append(guess) # adds a guessed letter to the list of guessed_letters

        if guess in word_hangman: # if the letter guessed is in the unknowned word
            print(f"The letter '{guess}' is in the word!")
        else:
            print(f"The letter '{guess}' is not in the word.")
            wrong_guesses += 1 # increases the wrong guesses by 1

        if all(letter in guessed_letters for letter in word_hangman):
            print(f"Correct, the word was '{word_hangman}'!")
            best_scores_hangman.append(wrong_guesses) # adds the scores to the list
            best_scores_hangman.sort()  # sort by lowest 3 as less mistakes is better
            best_scores_hangman = best_scores_hangman[:3]  # Keep top 3
            break
    else:
        print(f"Game over, the word was '{word_hangman}'.")

    if input("Play again? (yes/no): ").strip().lower() == 'yes': # asks user if they want to play it again
        play_hangman() # calls the function again
    else:
        print("Thanks for playing!")



