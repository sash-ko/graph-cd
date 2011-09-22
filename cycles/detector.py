#!/usr/bin/python

from pygraph.algorithms.traversal import traversal
from pygraph.classes.digraph import digraph

def detect(g):
    index = {}
    lowlink = {}
    components = []
    stack = []

    for n in g.nodes():
        if n not in index:
            dfs(g, n, index, lowlink, stack)

def dfs(g, node, index, lowlink, stack):
    l = len(index)
    index[node] = l
    lowlink[node] = l
    stack.append(node)
    root = True

    neighbors = g.neighbors(node)
    if neighbors:
        for n in neighbors:
            if n not in index:
                dfs(g, n, index, lowlink, stack)
            if lowlink[node] > lowlink[n]:
                lowlink[node] = lowlink[n]
                root = False
            #    lowlink[node] = min(lowlink[node], lowlink[n])
            #elif n in stack:
            #    lowlink[node] = min(lowlink[node], index[n])

        #if lowlink[node] == index[node]:
        if root:
            component = []

            while True:
                n = stack.pop()
                component.append(n)
                if n == node:
                    break
            print component

if __name__ == '__main__':

    g = digraph()
    g.add_nodes([0, 1, 2, 3, 4, 5])
    g.add_edge((0, 1))
    g.add_edge((0, 2))
    g.add_edge((1, 3))
    g.add_edge((1, 4))
    g.add_edge((2, 5))

    detect(g)
