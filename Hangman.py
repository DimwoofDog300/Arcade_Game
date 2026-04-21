import random


def get_word_hangman(): # function that gets a word based on users entered theme
    fruits = ['apple', 'watermelon', 'mango', 'strawberry', 'blueberry', 'orange', 'durian', 'lychee', 'jackfruit']
    weapons = ['flamethrower', 'assault rifle', 'bow', 'crossbow', 'minigun', 'knife', 'katana']
    while True:
        theme = input("Welcome to hangman, choose a theme. Input either 'fruits' or 'weapons'").lower() # Asks input for a theme
        if theme == 'fruits':
            pick_fruits = random.choice(fruits) # chooses a random word from the fruits list
            return pick_fruits
        elif theme == 'weapons':
            pick_weapons = random.choice(weapons)
            return pick_weapons # chooses a random word from the weapons list
        else:
            print("Invalid input, either input 'fruits' or 'weapons'")

def play_hangman(): # Function to play the game
    word_hangman = get_word_hangman() # calls the function to get a word
    guessed_letters = [] # makes a empty list
    wrong_guesses = 0 # Sets your guesses to 0
    max_wrong = 6 # Sets a boundry on how many incorrect answers you allowed to have

    print(f"The word is {len(word_hangman)} letters long and you have 6 guesses") # lists the length of the word you need to guess

    while wrong_guesses < max_wrong: # While loop that works when you
        for letter in word_hangman: # For each letter in the word chosen
            if letter in guessed_letters: #
                print(letter, end=' ')
            else:
                print('_', end=' ')

        if guessed_letters:
            print("Guessed letters:", ', '.join(guessed_letters))
        else:
            print("Guessed letters: None")

        print(f'Guesses remaining: {max_wrong - wrong_guesses}')

        try:
            guess = input('Guess a letter: ').lower().strip()
            if len(guess) != 1 or not guess.isalpha():
                raise ValueError("Please enter a single letter.")
            if guess in guessed_letters:
                raise ValueError(f"You have already guessed '{guess}', try another.")
        except ValueError:
            continue


        guessed_letters.append(guess) # adds a guessed letter to the list of guessed_letters

        if guess in word_hangman:
            print(f"The letter '{guess}' is in the word!")
        elif guess == '!':
            main()
        else:
            print(f"The letter '{guess}' is not in the word.")
            wrong_guesses += 1

        if all(letter in guessed_letters for letter in word_hangman):
            print(f"Correct, the word was '{word_hangman}'!")
            break
    else:
        print(f"Game over, the word was '{word_hangman}'.")

    if input("Play again? (yes/no): ").strip().lower() == 'yes':
        play_hangman()
    else:
        print("Thanks for playing!")

    play_hangman() # runs the function