#1. import the wanted Python module

import random

#2. Pick and save the words to be guessed as a list in Hangman_guessing.py file
#Note : (all the words to be guessed consist of six letters)

from hangman_guessing import guess_list

#3. Use the imported Python module to pick a random word from the words you save.

guessing_word = random.choice(guess_list)

word_letters = len(guessing_word)

#4. Keep the game running untill the game is over

game_over = False
tries = 6