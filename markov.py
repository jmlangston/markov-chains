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

dictionary = make_chains(opened_file)

# dictionary = make_chains(opened_file)
# print dictionary    

def make_text(dictionaryv2):
    """Takes dictionary of markov chains; returns random text."""
    our_string = ""
    for index in dictionaryv2: 
        random_key = random.choice(dictionaryv2.keys())
        print random_key
        value2 = dictionaryv2[random_key]
        random_value = random.choice(value2)
        print random_value
        new_key = (random_key[1], random_value)
        print new_key
        new_value = random.choice(new_key)
        our_string = our_string + random_key[0] + random_key[1] + new_value

    if new_key not in dictionaryv2:
        False

    # return "Here's some random text."

make_text(dictionary)

# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

# input_text = "Some text"

# # Get a Markov chain
# chain_dict = make_chains(input_text)

# # Produce random text
# random_text = make_text(chain_dict)

# print random_text
