import json
import random
import string

#from words import words
#this is if done with words.py with the same data.

with open('words.json', 'r') as file:
    rawdata = json.load(file)

#testing
#word_abandoned = rawdata['data'][2]
#print(f"{word_abandoned} \n")

words = rawdata['data']
print(type(words))
print(len(words))

def get_right_words(words):
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_right_words(words)
    word_letters = set(word) #to store letters of the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    while(len(word_letters>0)):
        print("You have used these letters:", " ".join(used_letters))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        
        elif user_letter in used_letters:
            print("You have already guessed this letter. :/")

        else:
            print("It is an invalid character. Please try again.")