#!/usr/bin/env python3
"""Interface to use Yolov3"""
#Cloning darknet in the home/github folder
# git clone https://github.com/pjreddie/darknet
# cd darknet
# make
# wget https://pjreddie.com/media/files/yolov3.weights
#Example
# ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg

import os
import argparse
DESCRIPTION = """
This command allows the user to use a Yolo classifier
from darknet to identify the object in a picture. The
only required input is the file path. You can also set
the noise threshold adding -t. Then, the program ask
you to insert the desired percentage. Default is 25%.
An error is returned if the file doesn't exist.
"""


def process(inpfile, thresh):
    """File preocessing"""

    ipath = os.getcwd()
    if not os.path.exists('{0}/{1}'.format(ipath,inpfile)):
        return 1

    os.system('cp {0} ~/github/darknet/data'.format(inpfile))
    os.chdir('/home/dario/github/darknet')
    os.system('./darknet detector test cfg/coco.data cfg/yolov3.cfg yolov3.weights data/{0} -thresh {1}'.format(inpfile, thresh))
    os.system('cp predictions.jpg {0}'.format(ipath))
    os.system('rm predictions.jpg')
    os.chdir('/home/dario/github/darknet/data')
    os.system('rm {0}'.format(inpfile))
    os.chdir(ipath)
    os.system('xdg-open predictions.jpg')

    return 0

def cli():
    PARSER = argparse.ArgumentParser(
        prog='darkYolo',
        formatter_class=argparse.RawTextHelpFormatter,
        description='darkYolo\n' + DESCRIPTION,
        epilog="Further information:\nhttps://pjreddie.com/darknet/yolo")
    PARSER.add_argument('inpfile', type=str, help='path to the input file')
    PARSER.add_argument('-t', '--thresh', action='store_true', help='thresh')
    ARGS = PARSER.parse_args()

    if ARGS.thresh:
        thresh = float(input('Set the thresh level: '))
        if ((thresh>1)&(thresh<100)):
            thresh = thresh/100
    else:
        thresh = 0.25

    if not((thresh>0)&(thresh<1)):
        print('Default level selected: 25%.')
        thresh = 0.25

    STAT = process(ARGS.inpfile, thresh)
    if STAT == 0:
        print('The work is done.')
    elif STAT == 1:
        print("The file doesn't exist.")

if __name__ == "__main__":
    cli()
