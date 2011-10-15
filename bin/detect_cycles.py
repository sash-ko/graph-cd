#!/usr/bin/python

import sys
import argparse
from pygraph.readwrite.dot import read
try:
    from cycles.detector import detect
except:
    sys.path.append('')
    from cycles.detector import detect

def main(args):
    with open(args.file) as f:
        g = read(''.join(f.readlines()))
    components = detect(g)
    if args.output:
        with open(args.output, 'w') as f:
            f.write(str(components))
    else:
        sys.stdout.write(str(components))

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True)
    parser.add_argument('-o', '--output')

    args = parser.parse_args()
    main(args)
