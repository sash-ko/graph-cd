#!/usr/bin/python

import argparse
from pygraph.readwrite.dot import read
try:
    from cycles.detector import detect
except:
    import sys
    sys.path.append('')
    from cycles.detector import detect

def main(args):
    with open(args.file) as f:
        g = read(''.join(f.readlines()))
    detect(g)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True)
    parser.add_argument('-o', '--output')

    args = parser.parse_args()
    main(args)
