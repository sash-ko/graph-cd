#!/usr/bin/python

from pygraph.classes.digraph import digraph
import tarjan

def detect(g):
    if isinstance(g, digraph):
        return tarjan.detect(g)
    raise Exception('Only directed graphs supported!')
