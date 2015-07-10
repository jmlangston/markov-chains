import sys
from random import choice

class SimpleMarkovGenerator(object):

    def __init__(self, files):
        read_files_output = self.read_files(files)
        make_chains_output = self.make_chains(read_files_output)
        self.dictionary = make_chains_output


    def read_files(self, filenames):
        master_list = []

        for f in filenames:
            opened_file = open(f).read().split()
            master_list += opened_file
            all_text = " ".join(master_list)
        return all_text


    def make_chains(self, astring):
        """Takes input text as string; returns dictionary of markov chains."""

        list_of_words = astring.split()

        dict_tuples = {}

        for i in range(len(list_of_words)-2):
            key = (list_of_words[i], list_of_words[i+1])
            value = list_of_words[i+2]

            if key not in dict_tuples:
                dict_tuples[key] = []

            dict_tuples[key].append(value)

        return dict_tuples


    def make_text(self):
        """Takes dictionary of markov chains; returns random text."""
        markov_dictionary = self.dictionary

        key = choice(markov_dictionary.keys())
        value = []

        while key in markov_dictionary:
            value2 = choice(markov_dictionary[key])
            value.append(value2)
            key = (key[1], value2)
            # if value > 100:
            #     break

        print " ".join(value)
         

filenames = sys.argv[1:]
My_Markov = SimpleMarkovGenerator(filenames)
My_Markov.make_text()




    # # Change this to read input_text from a file, deciding which file should
    # # be used by examining the `sys.argv` arguments (if neccessary, see the
    # # Python docs for sys.argv)

    # input_text = "Some text"

    # # Get a Markov chain
    # chain_dict = make_chains(input_text)

    # # Produce random text
    # random_text = make_text(chain_dict)

    # print random_texts
