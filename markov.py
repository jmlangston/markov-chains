import sys
import random

opened_file = open('green-eggs.txt')
# print type(opened_file)

def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""

    list_of_words = corpus.read().replace("\n", " ").split()
    # print type(corpus)
    # print type(list_of_words)

    dict_tuples = {}

    for i in range(len(list_of_words)-2):
        key = (list_of_words[i], list_of_words[i+1])
        value = list_of_words[i+2]

        if key not in dict_tuples:
            dict_tuples[key] = []

        dict_tuples[key].append(value)

        # if list_of_words[third_word] == list_of_words[-1]:
        #     print dict_tuples
        #     return
        # else: 
        #     value = dict_tuples.get([key], value.append(list_of_words[third_word]))
        #     first_word += 1
        #     second_word += 1
        #     third_word += 1

        # if tuple_pair not in dict_tuples:
        #     list_of_following_words = []
        #     dict_tuples[tuple_pair] = list_of_following_words.append(third_word)
        # if tuple_pair in dict_tuples:
        #     dict_tuples[tuple_pair] = # ad

    return dict_tuples

make_chains(opened_file)

# dictionary = make_chains(opened_file)
# print dictionary    

def make_text(dict_tuples):
    """Takes dictionary of markov chains; returns random text."""
    # make_chains(opened_file) 
    # http://stackoverflow.com/questions/16043797/python-passing-variables-between-functions
    print dict_tuples
    # random.sample(make_chains(opened_file),1)

    # return "Here's some random text."

make_text(dict_tuples)

# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

# input_text = "Some text"

# # Get a Markov chain
# chain_dict = make_chains(input_text)

# # Produce random text
# random_text = make_text(chain_dict)

# print random_text
