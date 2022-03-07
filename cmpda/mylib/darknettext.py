#!/usr/bin/env python3
"""Interface to use RNN text generator"""
#Cloning darknet in the home/github folder
# git clone https://github.com/pjreddie/darknet
# cd darknet
# make
#Example
# ./darknet rnn generate cfg/rnn.cfg <weights>

import os
import argparse
from random import randint

RAND = randint(0, 1000)
DESCRIPTION = """
This command allows the user to generate a random text
of a given author (KANT by default) using a RNN by darknet.
The allowed authors are:
-) kant
-) shakespeare
-) tolstoy
It gives an error if a different input author is passed."""

def process(author, len, rand, seed):
    ipath = os.getcwd()
    os.chdir('/home/dario/github/darknet')
    basic = f'./darknet rnn generate cfg/rnn.cfg {author}.weights '
    options = f'-len {len} -srand {rand} -seed {seed}'
    os.system(basic + options)
    os.chdir(ipath)
    return 0

def cli():
    PARSER = argparse.ArgumentParser(
        prog='darkText',
        formatter_class=argparse.RawTextHelpFormatter,
        description='darkText\n' + DESCRIPTION,
        epilog="Further information:\nhttps://pjreddie.com/darknet/rnns-in-darknet")
    PARSER.add_argument('-author', type=str, default='kant', help='author of the text')
    PARSER.add_argument('-len', type=int, default=1000, help='text lenght')
    PARSER.add_argument('-rand', type=int, default=RAND, help='random seed')
    PARSER.add_argument('-seed', type=str, default='\n', help='first word of the text')
    ARGS = PARSER.parse_args()

    STAT = process(*vars(ARGS).values())
    if STAT == 0:
        print('The work is done.')
    elif STAT == 1:
        print("The file doesn't exist.")

if __name__ == "__main__":
    cli()
