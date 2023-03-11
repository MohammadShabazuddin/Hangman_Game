import random
import string
from Words import words
def get_valid_word(words):
    word= random.choice(words)
    while '-' in word or ' ' in word:
        word= random.choice(words) # randomly chooses something form the list
    return word.upper()

def hangman():
    
    word = get_valid_word(words)
    word_letters = set(word) #Letters in the world
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user have guessed 

    lives = 12
    # get user input 
    while len(word_letters) > 0 and lives > 0:
        #Letters already used
        #' '.join(['a','b','cd']) --> 'a b cd'
        print('You have', lives, ' lives left and You have used these letters: ',' '.join(used_letters))

        #What current word is (ie W - R D)
        word_list = [letter if letter in used_letters  else '-' for letter in word]
        print('Current word: ',' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 # Take away a life if worng
                print("letter is not in the word")
        elif user_letter in used_letters:
            print("you have already used that character. please try again.")

        else:
            print('Invalid character. please try again')
    
    # gets here when len(word_letters) == 0 and lives == 0
    if lives == 0:
        print('You are dead, Sorry. The word was', word)
    else:
        print("congratulations!! You guessed the word", word, '***!WINNER!**')




hangman()





 