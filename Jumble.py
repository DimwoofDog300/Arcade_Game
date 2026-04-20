import random

def choose():
    words = ['cat', 'dog']
    pick = random.choice(words)
    return pick

def jumble(words):
    random_word = random.sample(words, len(words))
    jumbled = ''.join(random_word)
    return jumbled

def play_jumble():
    while True:
        try:
            rounds_jumble = int(input("How many rounds of Jumble would you like to play? "))
            print(f"You have chosen to play {rounds_jumble} rounds")
            break
        except ValueError:
            rounds_jumble = int(input("How many rounds of Jumble would you like to play? "))

    score_jumble = 0

    for i in range(rounds_jumble):
        picked_word = choose()
        jumbled_word = jumble(picked_word)
        print(jumbled_word)

        answer = input("What is the word").strip().lower()

        if answer == picked_word:
            print("Correct")
            score_jumble += 1
        else:
            print("incorrect")
    print("Game over")


play_jumble()