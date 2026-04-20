import random

def choose():
    words = ['cat', 'dog']
    pick = random.choice(words)
    return pick

def jumble(words):
    random_word = random.sample(words, len(words))
    jumbled = ''.join(random_word)
    print(jumbled)

def play_jumble():
    while True:
        while True:
            try:
                rounds_jumble = int(input("How many rounds of Jumble would you like to play? "))
                print(f"You have chosen to play {rounds_jumble} rounds")
                break
            except ValueError:
                rounds_jumble = int(input("How many rounds of Jumble would you like to play? "))
        for i in rounds_jumble:
            score_jumble = 0
            picked_word = choose()
            jumbled_word = jumble(picked_word)
            answer = input("What is the word")
            if answer == jumbled_word:
                score_jumble += 1
            else:
                print("incorrect")