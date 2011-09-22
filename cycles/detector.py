#!/usr/bin/python

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

if __name__ == '__main__':

    from pygraph.classes.digraph import digraph

    g = digraph()
    #g.add_nodes([0, 1, 2, 3, 4, 5])
    #g.add_edge((0, 1))
    #g.add_edge((0, 2))
    #g.add_edge((1, 3))
    #g.add_edge((1, 4))
    #g.add_edge((2, 5))
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

    assert detect(g) == [[7], [5, 6], [3, 2], [4, 1, 0]]

    #0   -   7
    #|       |
    #1 - 5   6
    #|   |   |
    #2 - 3 - 4

    g = digraph()
    g.add_nodes(range(0, 8))
    g.add_edge((0, 1))
    g.add_edge((1, 2))
    g.add_edge((2, 3))
    g.add_edge((3, 4))
    g.add_edge((3, 5))
    g.add_edge((4, 6))
    g.add_edge((5, 1))
    g.add_edge((6, 7))
    g.add_edge((7, 0))
    print detect(g)
