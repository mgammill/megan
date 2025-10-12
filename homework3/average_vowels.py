# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.

def counting_vowels_and_consonants(text):
    vowels = 0
    consonants = 0
    for character in text:
        if character.isalpha():
            if character in ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U"):
                vowels += 1
            else:
                consonants += 1
    return(vowels, consonants)

# print(counting_vowels_and_consonants("My name is Megan and I am a Math Major!"))

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

def split_text_into_sentences(text):
    split1 = text.split(".") # This will split the inputted text into a list of strings, where each string is separated by a "."
    split2 = []
    split3 = []
    for string in split1:
        sublist = string.split("!") # This will split each string from list 1 into a list of substrings, where each substring was separated by a "!"
        for entry in sublist:
            split2.append(entry) # Now we have a list (list2) of strings separated by a "." or "!"
    for string in split2:
        sublist = string.split("?") # This will split the inputted text into a list of strings, where each string is separated by a "?"
        for entry in sublist:
            if entry != "":
                split3.append(entry) # This generates a list (list3) of strings, where each string is separated by a ".", "!", or "?", and no string is empty
    return(split3)

def average_vowels_and_consonants(text):
    sentences = split_text_into_sentences(text) # This defines the list "sentences" as a list of strings, where each string is a sentence from the inputted text.
    number_of_sentences = len(sentences) # The length of the list "sentences" returns the number of sentences in the inputted text
    total_number_of_vowels = counting_vowels_and_consonants(text)[0]
    total_number_of_consonants = counting_vowels_and_consonants(text)[1]
    average_number_of_vowels = (total_number_of_vowels / number_of_sentences)
    average_number_of_consonants = (total_number_of_consonants / number_of_sentences)
    return(number_of_sentences, average_number_of_vowels, average_number_of_consonants)

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)
print(split_text_into_sentences(paragraph))
print(average_vowels_and_consonants(paragraph))
# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

