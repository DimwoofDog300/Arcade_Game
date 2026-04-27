import random
import time

best_scores_jumble = [] # makes a empty list as no scores have been added

def choose(): # A function to choose a word from a list of words
    words = ['cat', 'dog', 'rainbow', 'apple', 'cheese', 'book'] # List of words to choose from
    pick = random.choice(words) # Picks randomly a word from the list
    return pick # Returns the randomly picked word

def jumble(words): # Function to get that random word and then jumble it up
    random_word = random.sample(words, len(words)) # gets the word and the length of it
    jumbled = ''.join(random_word) # Joins the word randomly
    return jumbled # Returns the jumbled word

def show_scores_jumble():
    if len(best_scores_jumble) > 0: # detects if the length of the list has more than 1 values in it
        print('JUMBLE SCORES LEADERBOARD')
        for i, score in enumerate(best_scores_jumble, 1): # pairs the list with a number and prints out the score
            print(f"{i}. {score} correct")
            print('')
        else: # If there is no items in list
            print("No jumble scores yet.")
            print('')


def play_jumble(): # Function that allows user to play the game
    global best_scores_jumble

    print('Jumble is a game where you get a jumbled word and you will need to try to guess the orginal word.')
    print('You have 10 rounds and try to guess as many words as you can correctly')

    time.sleep(1)

    score_jumble = 0 # Sets the score to 0

    for i in range(10): # Loops the amount of times based on the rounds they inputted
        picked_word = choose() # Calls the function to choose a word
        jumbled_word = jumble(picked_word) # Call the function to scramble the word
        print(jumbled_word) # Output the word

        answer = input("What is the unjumbled word: ").strip().lower() # Asks user for word

        if answer == picked_word: # If it is the same, then is correct
            print("Correct")
            score_jumble += 1 # Increases score by 1
        else: # If they got it wrong print incorrect
            print("Incorrect")

    best_scores_jumble.append(score_jumble) # adds the score to the list
    best_scores_jumble.sort(reverse=True)  # sorts the scores highest to lowest
    best_scores_jumble = best_scores_jumble[:3] # makes it so that the first 3 items which were just sorted to highest to lowest is chosen

    print("Game over") # if rounds run out, then game is over


