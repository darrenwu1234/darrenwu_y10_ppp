import nltk
from nltk.corpus import words

# Download the word list if you haven't already
nltk.download('words')

# Create a set of valid words
valid_words = set(words.words())

def is_valid_word(word):
    return word.lower() in valid_words

# Example usage
word_to_check = "hel"
if is_valid_word(word_to_check):
    print(f"{word_to_check} is a valid word.")
else:
    print(f"{word_to_check} is not a valid word.")