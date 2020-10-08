"""First assignment: reads a text.txt file and prints the relative frequencies of the characters."""

import argparse
import logging
import time
import string
import matplotlib.pyplot as plt


def process(file_path):

    """Prepares the working copy of the file."""
    switch = input('Change the beginning and the ending of the text?(S/n) ')
    if switch == 'S':
        start = int(input('From which line do you want to start?  '))
        end = int(input('At which line do you want to stop? '))
        if start < 1:
            start = 1
        if start > end:
            return 1
    else:
        start = 1
        end = 0

    logging.info('Reading input file %s...', file_path)
    with open(file_path) as input_file:
        i = 1
        while i < start:
            i += 1
            input_file.readline()
        logging.info('The starting line is %d.', i)
        with open('workfile.txt', 'w') as workfile:
            while True:
                i += 1
                line = input_file.readline()
                workfile.write(line)
                if (i == end + 1) or (line == ''):
                    break
    num_lines = i - start

    with open('workfile.txt', 'r') as workfile:
        text = workfile.read()
    logging.info('The working copy is ready.')
    start_time = time.time()

    """Creats a dictionary of letter frequencies and counts the words."""
    num_words = 0
    char_f = {ch: 0 for ch in string.ascii_lowercase}
    for char in text:
        char = char.lower()
        if char in char_f:
            char_f[char] += 1
        if char in  (' ', '\n'):
            num_words += 1

    """Output and graph."""
    num_letters = sum(char_f.values())
    if num_letters == 0:
        return 2
    print(f'The total number of letters is {num_letters}.')
    print(f'The total number of words is {num_words}.')
    print(f'The total number of lines is {num_lines}.')
    print('Relative frequencies of the letters:')
    for char, num in char_f.items():
        print(f'{char} -->  {num/num_letters:.3}')
    time_elapsed = time.time()- start_time
    print(f'Done in {time_elapsed:.3} seconds')
    switch = input('Do you want to see the results on a bar graph?(S/n) ')
    if switch == 'S':
        plt.xlabel('Character')
        plt.ylabel('Frequency')
        plt.title('Frequencies of the letters in the text')
        plt.bar(char_f.keys(), char_f.values())
        plt.show()
    return 0


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('inpfile', type=str, help='Path to the input file')
    PARSER.add_argument('-v', '--verbose', action='store_true', help='DEBUG')
    ARGS = PARSER.parse_args()

    if ARGS.verbose:
        logging.basicConfig(level=logging.DEBUG)
        logging.info('Logging level set on DEBUG.')

    STATE = process(ARGS.inpfile)
    if STATE == 1:
        print('The ending line cannot come before the starting one!!!')
    elif STATE == 2:
        print('There are no letters in the text.')
    else:
        print('The work is done.')
