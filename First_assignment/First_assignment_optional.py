"""First assignment: reads a text.txt file and prints the relative frequencies of the characters."""

import argparse
import logging
import time
import string
import matplotlib.pyplot as plt



def process(file_path):
    """Prepares the working file."""
    s = input('Do you want to change the beginning and the ending of the text?(S/n) ')
    if (s == 'S'):
        start = int(input('From which line do you want to start?  '))
        end = int(input('At which line do you want to stop? '))
        if start < 1 : start = 1
        if start > end : raise ValueError('The end line cannot come before the starting one!!!')
    else:
        start = 1
        end = 100
        """Here i've some problems."""
    num_lines = end - start + 1
    logging.info(f'Reading input file {file_path}...')
    with open(file_path) as input_file:
            for i in range(start-1):
                input_file.readline()
            with open('workfile.txt','w') as workfile:
                for i in range(num_lines):
                    workfile.write(input_file.readline())
    with open('workfile.txt','r') as workfile:
            text = workfile.read()
    start_time = time.time()

    """Creats a dictionary of letter frequencies and counts the words."""
    num_words = 0
    char_f = {ch: 0 for ch in string.ascii_lowercase}
    for ch in text:
        ch = ch.lower()
        if ch in char_f: char_f[ch] += 1
        if ch == ' ' or ch == '\n' : num_words += 1
        """Good assumption?"""

    """Output and graph."""
    num_letters = sum(char_f.values())
    if num_letters == 0 :
        print('There are no letters in the text.')
        return
    print(f'The total number of letters is {num_letters}.')
    print(f'The total number of words is {num_words}.')
    print(f'The total number of lines is {num_lines}.')
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
