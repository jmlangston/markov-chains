import sys
import random

opened_file = open('green-eggs.txt')

def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""

    list_of_words = corpus.read().replace("\n", " ").split()

    dict_tuples = {}

    for i in range(len(list_of_words)-2):
        key = (list_of_words[i], list_of_words[i+1])
        value = list_of_words[i+2]

        if key not in dict_tuples:
            dict_tuples[key] = []

        dict_tuples[key].append(value)

    return dict_tuples

dictionary = make_chains(opened_file)


def make_text(markov_dictionary):
    """Takes dictionary of markov chains; returns random text."""

    key = random.choice(markov_dictionary.keys())
    value = []

    while key in markov_dictionary:
        value2 = random.choice(markov_dictionary[key])
        value.append(value2)
        key = (key[1], value2)
        print key
        # if value > 100:
        #     break

    print " ".join(value)
     

make_text(dictionary)

# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

input_text = "Some text"

# Get a Markov chain
chain_dict = make_chains(input_text)

# Produce random text
random_text = make_text(chain_dict)

print random_texts
