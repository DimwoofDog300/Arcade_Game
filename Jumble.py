import random


def choose(): # A function to choose a word from a list of words
    words = ['cat', 'dog', 'rainbow', 'apple', 'cheese', 'book'] # List of words to choose from
    pick = random.choice(words) # Picks randomly a word from the list
    return pick # Returns the randomly picked word

def jumble(words): # Function to get that random word and then jumble it up
    random_word = random.sample(words, len(words)) # gets the word and the length of it
    jumbled = ''.join(random_word) # Joins the word randomly
    return jumbled # Returns the jumbled word

def show_scores_jumble():
    if len(best_scores_jumble) > 0:
        print('JUMBLE SCORES LEADERBOARD')
        for i, score in enumerate(best_scores_jumble, 1):
            print(f"{i}. {score} correct")
        else:
            print("No jumble scores yet.")


def play_jumble(): # Function that allows user to play the game
    global best_scores_jumble

    while True: # Repeats the while loop
        try:
            rounds_jumble = int(input("How many rounds of Jumble would you like to play? ")) # asks how round user wants to play
            print(f"You have chosen to play {rounds_jumble} rounds") # displays how rounds the user is playing
            break # exits the loop
        except ValueError:
            print('Remember to input a integer to choose how many rounds to play')
            continue

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
            print("go back to main")
        else: # If they got it wrong print incorrect
            print("Incorrect")

    best_scores_jumble.append(score_jumble)
    best_scores_jumble.sort(reverse=True)  # Higher is better for jumble
    best_scores_jumble = best_scores_jumble[:3]

    print("Game over") # if rounds run out, then game is over


