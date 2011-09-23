#!/usr/bin/python

"""
Tarjan's strongly connected components algorithm.

NOTE: for directed graphs only!
"""

def detect(g):
    index = {}
    lowlink = {}
    components = []
    stack = []

    for n in g.nodes():
        if n not in index:
            dfs(g, n, index, lowlink, stack, components)
    return components

def dfs(g, node, index, lowlink, stack, components):
    l = len(index)
    index[node] = l
    lowlink[node] = l
    stack.append(node)

    neighbors = g.neighbors(node)
    for n in neighbors:
        if n not in index:
            dfs(g, n, index, lowlink, stack, components)
            lowlink[node] = min(lowlink[node], lowlink[n])
        elif n in stack:
            lowlink[node] = min(lowlink[node], index[n])

    if lowlink[node] == index[node]:
        component = []

        while True:
            n = stack.pop()
            component.append(n)
            if n == node:
                break
        components.append(component)
