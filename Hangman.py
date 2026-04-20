import random
from Main import main

def get_word_hangman():
    fruits = ['apple', 'watermelon', 'mango', 'strawberry', 'blueberry', 'orange', 'durian', 'lychee', 'jackfruit']
    weapons = ['flamethrower', 'assault rifle', 'bow', 'crossbow', 'minigun', 'knife', 'katana']
    while True:
        theme = input("Welcome to hangman, choose a theme. Input either 'fruits' or 'weapons'").lower()
        if theme == fruits:
            pick_fruits = random.choice(fruits)
            return pick_fruits
        elif theme == weapons:
            pick_weapons = random.choice(weapons)
            return pick_weapons
        else:
            print("Invalid input, either input 'fruits' or 'weapons'")

def play_hangman():
    word_hangman = get_word_hangman()
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print(f"The word is {len(word_hangman)} letters long and you have 6 guesses")

    while wrong_guesses < max_wrong:
        for letter in word_hangman:
            if letter in guessed_letters:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        print()

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
        except ValueError as e:
            print(e)
            continue

        guessed_letters.append(guess)

        if guess in word_hangman:
            print(f"The letter '{guess}' is in the word!")
        elif guess == !:
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

    play_hangman()