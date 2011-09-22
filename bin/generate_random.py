#!/usr/bin/python

import argparse
from pygraph.algorithms.generators import generate
from pygraph.readwrite.dot import write
from pygraph.algorithms.cycles import find_cycle

def main(args):
    g = generate(args.nodes, args.edges, True)

    while not find_cycle(g):
        g = generate(args.nodes, args.edges, True)

    with open(args.output, 'w') as f:
        f.write(write(g))

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', required=True)
    parser.add_argument('-n', '--nodes', default=100)
    parser.add_argument('-e', '--edges', default=200)
    #parser.add_argument('-c', '--force_cycles', default=True)

    args = parser.parse_args()
    main(args)
