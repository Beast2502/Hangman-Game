#1. import the wanted Python module

import random

#2. Pick and save the words to be guessed as a list in Hangman_guessing.py file
#Note : (all the words to be guessed consist of six letters)

from hangman_guessing import guess_list

#3. Use the imported Python module to pick a random word from the words you save.

guessing_word = random.choice(guess_list).lower()

word_letters = len(guessing_word)

#4. Keep the game running untill the game is over

game_over = False
#5. Apply tries to the players to use to try to win
tries = 6

#6. Save game shapes in hangman_life.py and import those shapes from this file

from hangman_life import game_name
print(game_name)

#7. Test the code you written untill now using Python print function

#print(f'The  word you gussed is {guessing_word}')

#8. Create a list contain six '_' underscore to store and save the right letter guessed by
result =[]
for i in range(word_letters):
    result += '_'

#9. Iterate over the player input  to keep the game running until the game is over
while not game_over:
    user_guessing  = input('Guess a letter => ')

#10. Inform the players about the letter they have guessed after they doo
    if user_guessing in result:
        print(f'The letter you have guessed is {user_guessing}')

#11 . Check  if the guessed letters by the players is right or wrong
    for position in range(word_letters):
        
        letter = guessing_word[position]
        if letter == user_guessing:
            result[position]= letter

#12. The player lose a try if they guessed wrong letter
    if user_guessing not in guessing_word:
        print(f'You gussed {user_guessing}, This letter is not in the word , you loose a try')

#13. If the players lose all their tries end game and print the end game message

        tries -=1
        if tries == 0:
            game_over =True
            print('\nGame over , You lose the game , Try again later\n')
            print(f'The  word  is {guessing_word}')

            
    
#14. Join all the letters which in the list of guessed letter and turn it into string.
    print(f'{" ".join(result) }')


#15.  Check if the player guessed all the right letter so end game and print the win message.
    if '_' not in result:
        game_over = True
        print('You are a winner , Congratulation')
        print(f'The  word you gussed is {guessing_word}')


#16 .  You print the correct shape after every player try.
    from hangman_life import lives
    print(lives[tries])




