"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()
    #return 'Contents of your file as one long string'
    return contents


def make_chains(text_string): # let's make dict chains with bi-grams

    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.
    # {tup(word1, word2):list[....]}

    }
    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    my_chain = ()
    my_list = []
    # your code goes here
    for words in text_string:
        my_chain = text_string.split()
     
 #   print(my_chain)
 #    i = index my_chain elements generated all KEYS
    for i in range(len(my_chain)-2):
        print('KEYS: ',my_chain[i], my_chain[i+1],'i=',i)
        print('==>>i+2',my_chain[i+2])
        my_list.append(my_chain[i+2])
        chains[(my_chain[i], my_chain[i+1])] = my_list
 
    # creating list for each KEY in Dict
    for key, value in chains.items():
        print("1", chains.keys())
        print("2", my_list.append(key))
        print('3-list of each KEY: ',key,"Values:", value)

    for i in range(len(my_chain)-1):
        
        print("4",my_chain[i],type(my_chain[i]), my_chain[i+1],'i=',i)
              # my_list.append(key[1])
            # c hains[(my_chain[i], my_chain[i+1])] = my_list
                   
    return print("chains: ", chains)


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

