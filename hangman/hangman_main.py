# p138

# main hangman

import p138_hangman
import opponent

print("Welcome to Hangman\n")

word = opponent.choice(0)

# game start
# player2
p138_hangman.hangman(word)
