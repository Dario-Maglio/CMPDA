"""First assignment."""

import argparse
import logging
import time
import string

logging.basicConfig(level = logging.DEBUG)

def process(file_path):
    """Reads a text file and compile the latter statistics."""
    start_time = time.time()

    logging.info('Reading input file %s...', file_path)
    with open(file_path) as input_file:
        text = input_file.read()
    num_chars = len(text)
    logging.info('The number of characters is %d.', num_chars)

    #char_dict = {chr(x): 0 for x in range(ord('a'), ord('z')+1)}
    char_dict = {ch: 0 for ch in string.ascii_lowercase}
    for ch in text:
        ch = ch.lower()
        if ch in char_dict:
            char_dict[ch] += 1

        #try:
        #    char_dict[ch.lower()] += 1
        #except KeyError:
        #    pass

    time_elapsed = time.time()- start_time
    logging.info('Done in %.3f seconds', elapsed_time)
    num_letters = sum(char_dict.values())
    for ch, num in char_dict.items():
        print(f'{ch} -->  {num/num_letters:.3%}')



if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=str, help='Path to the input file')
    args = parser.parser_args()
    process(args.infile)
