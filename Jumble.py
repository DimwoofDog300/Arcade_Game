import random
from Main import main # Allows the main function to be used

def choose(): # A function to choose a word from a list of words
    words = ['cat', 'dog', 'rainbow', 'apple', 'cheese', 'book'] # List of words to choose from
    pick = random.choice(words) # Picks randomly a word from the list
    return pick # Returns the randomly picked word

def jumble(words): # Function to get that random word and then jumble it up
    random_word = random.sample(words, len(words)) # gets the word and the length of it
    jumbled = ''.join(random_word) # Joins the word randomly
    return jumbled # Returns the jumbled word



def play_jumble(): # Function that allows user to play the game
    while True: # Repeats the while loop
        try:
            rounds_jumble = int(input("How many rounds of Jumble would you like to play? "))
            print(f"You have chosen to play {rounds_jumble} rounds")
            break
        except ValueError:
            rounds_jumble = int(input("How many rounds of Jumble would you like to play? "))

    score_jumble = 0 # Sets the score to 0

    for i in range(rounds_jumble): # Loops the amount of times based on the rounds they inputted
        picked_word = choose() # Calls the function to choose a word
        jumbled_word = jumble(picked_word) # Call the function to scramble the word
        print(jumbled_word) # Output the word

        answer = input("What is the word").strip().lower() # Asks user for word

        if answer == picked_word: # If it is the same, then is correct
            print("Correct")
            score_jumble += 1 # Increases score by 1
        elif answer == '!': # If user inputs, return to menu
            main()
        else: # If they got it wrong print incorrect
            print("incorrect")
    print("Game over") # if rounds run out, then game is over


play_jumble()