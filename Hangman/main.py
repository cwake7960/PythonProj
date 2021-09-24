import random
from words import words
import string

def get_valid_words(words):
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)
     
    print(f"{word}")
    return word.upper()



def hangman():
    word = get_valid_words(words)
    print(f"{word}")
    word_letters = set(word)
    alaphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('You have ', lives, ' lives left, you have used these letters ', ' '.join(used_letters))
        #word_list = [letter if letter in used_letters else '-' for letter in word]
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input("guess a letter ").upper()
        if user_letter in alaphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives -1
                print("letter not in word")

        elif user_letter in used_letters:
            print("you already used that character, try agian")
        else:
            print("invalad character, try agian")
    
    if lives == 0:
        print('you died, the word was ', word)
    else:
        print(f"{word} \n you win ")

    input("press the anykey to exit")

hangman()
#get_valid_words(words)