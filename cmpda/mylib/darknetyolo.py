#!/usr/bin/env python3
"""Interface to use Yolov3"""

import os
import argparse


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
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('inpfile', type=str, help='Path to the input file')
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
