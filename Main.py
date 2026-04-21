# imports functions from other modules
from Jumble import play_jumble
from Hangman import play_hangman

def main(): # main function
    while True: # allows it to repeat infinitely
        print('Welcome to the arcade')
        print('Remember input ! in any game to exit it')
        game_choice = int(input('Input 1 for jumble, 2 for hangman and 3 for scores')) # Asks user what they want to play
        if game_choice == 1:
            play_jumble() # calls jumble function
        elif game_choice == 2:
            play_hangman() # calls hangman function
        elif game_choice == 3:
            print("scores")
        else:
            print('Remember to only input 1, 2 or 3')
            continue
main()