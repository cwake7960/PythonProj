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
    word_letters = set(word)
    alaphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0 :
        print('you have used these letters ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        user_letter = input("guess a letter ").upper()
        if user_letter in alaphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("you already used that character, try agian")
        else:
            print("invalad character, try agian")


hangman()
#get_valid_words(words)