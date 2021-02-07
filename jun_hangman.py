
import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from a list
    while '-' in word or ' ' in word:
        word = random.choice(word)

    return word

def hangman():
    word = get_valid_word(words)
    word_letter = set(word) #letter in the word 
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    #getting user input
    while len(word_letter) > 0:
        #letter used
        #' ' '.join(['a' 'b' 'c' ])
        print('you have to use these letters: ', ' '.join(used_letters))
        user_letter = input('guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)

        elif user_letter in used_letters:
            print('you has already used that letter, please try again')

        else:
            print('invaid letter, please try again')

    #get's here when len(word_letter) == 0

user_input = input('type something:')
print(user_input)