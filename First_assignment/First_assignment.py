"""First assignment: reads a text.txt file and prints the relative frequencies of the characters."""

import argparse
import logging
import time
import string
import matplotlib.pyplot as plt



def process(file_path):

    logging.info(f'Reading input file {file_path}...')
    with open(file_path) as input_file:
        text = input_file.read()

    start_time = time.time()
    num_chars = len(text)
    logging.info(f'The total number of characters is {num_chars}.')

    """Creats a dictionary of letter frequencies."""
    #char_dict = {chr(x): 0 for x in range(ord('a'), ord('z')+1)}
        #try:
        #    char_dict[ch.lower()] += 1
        #except KeyError:
        #   pass
    char_f = {ch: 0 for ch in string.ascii_lowercase}
    for ch in text:
        ch = ch.lower()
        if ch in char_f:
            char_f[ch] += 1

    num_letters = sum(char_f.values())
    logging.info(f'The total number of letters is {num_letters}.')

    """Prints and makes a graph of the results."""
    print('Relative frequencies of the letters:')
    for ch, num in char_f.items():
        print(f'{ch} -->  {num/num_letters:.3}')
    time_elapsed = time.time()- start_time
    print(f'Done in {time_elapsed:.3} seconds')
    s = input('Do you want to see the results on a bar graph?(S/n) ')
    if (s == 'S'):
        plt.xlabel('Character')
        plt.ylabel('Frequency')
        plt.title('Frequencies of the letters in the text')
        plt.bar(char_f.keys(), char_f.values())
        plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('inpfile', type = str, help = 'Path to the input file')
    parser.add_argument('-v','--verbose', action = 'store_true', help = 'Set the logging level to DEBUG')
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level = logging.DEBUG)
        logging.info('Logging level set on DEBUG.')
    process(args.inpfile)
