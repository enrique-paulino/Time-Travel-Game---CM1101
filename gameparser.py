import string

# List of "important" words. Please fill this list with any items or
# commands in the game.
imp_words = ['go', 'south', 'north', 'west', 'east', 'take', 'drop', 'use', 'device', 'sapling', '1staid', 'water', 'dogfood', 'fertilizer', 'key', 'seeds', 'puppy', 'youngtree', 'armingkey', 'shovel']


def filter_words(words, imp_words):
# Compares the two lists and returns the words found in both
    return [n for n in words if
             any(m in n for m in imp_words)]

def remove_punct(text):
# Removes all punctuation from the user_input
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char

    return no_punct


def normalise_input(user_input):

    # Remove punctuation and convert to lower case
    no_punct = remove_punct(user_input).lower()
    # Switches user_input from a string to a list
    no_punct = list(no_punct.split(" "))

    user_input = filter_words(no_punct, imp_words)
    # Removes "" from the final list
    return [s for s in user_input if s != ""]
