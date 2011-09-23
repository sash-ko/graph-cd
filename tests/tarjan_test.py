#!/usr/bin/python

from pygraph.classes.digraph import digraph

try:
    from cycles import tarjan
except:
    import sys
    sys.path.append('')
    from cycles import tarjan

def funcional_test():
    g = digraph()
    g.add_nodes(range(0, 8))
    g.add_edge((0, 1))
    g.add_edge((1, 2))
    g.add_edge((1, 4))
    g.add_edge((1, 5))
    g.add_edge((2, 3))
    g.add_edge((2, 6))
    g.add_edge((3, 2))
    g.add_edge((3, 7))
    g.add_edge((4, 0))
    g.add_edge((4, 5))
    g.add_edge((5, 6))
    g.add_edge((6, 5))
    g.add_edge((6, 7))
    g.add_edge((7, 7))

    assert tarjan.detect(g) == [[7], [5, 6], [3, 2], [4, 1, 0]]

