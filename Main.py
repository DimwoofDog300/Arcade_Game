# imports functions from other modules
from Jumble import play_jumble, show_scores_jumble
from Hangman import play_hangman, show_scores_hangman
import sys
import time



def main(): # main function
    while True: # allows it to repeat infinitely
        print('Welcome to the arcade')
        print('Remember input ! in any game to exit it')
        game_choice = input('Input 1 for jumble, 2 for hangman and 3 for scores and 4 for exiting the program: ') # Asks user what they want to play
        print('')
        if game_choice == '1':
            time.sleep(1)
            play_jumble() # calls jumble function
        elif game_choice == '2':
            time.sleep(1)
            play_hangman() # calls hangman function
        elif game_choice == '3':
            time.sleep(1)
            show_scores_hangman() # calls both functions and will show the scores of the games
            print('')
            show_scores_jumble()
        elif game_choice == '4':
            print('Exiting program')
            sys.exit() # finishes the code
        else:
            print('Invalid input, input 1 for jumble, 2 for hangman, 3 for scores and 4 to exit the program')
            time.sleep(1)
            continue
main()