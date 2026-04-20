from Jumble import play_jumble
from Hangman import play_hangman

def main():
    while True:
        game_choice = int(input('Input 1 for jumble, 2 for hangman and 3 for scores'))
        if game_choice == 1:
            play_jumble()
        elif game_choice == 2:
            play_hangman()