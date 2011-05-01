#!/usr/bin/env python

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def node_creator(lists, x, y):

    if lists[x][y] == None:
        return None

    return Node(lists[x][y],
                node_creator(lists, x+1, y),
                node_creator(lists, x+1, y+1)
                )

def graph_brute_force(node, path):

    (l, v, r) = (node.left, node.value, node.right)

    path = path + [v]
    
    if l == None or r == None:
        return path

    #left first
    return graph_brute_force(l, path) + graph_brute_force(r, path)

g = []
n = 0

with open("problem18_input.txt") as f:
    data = f.readlines();
    n = len(data)
    for line in data:
        l = line.strip().split(" ")
        l = [int(i) for i in l]
        g.append(l)
    # append a list with None to simply parsing
    g.append([None] * 2 * len(g[-1]))

g = node_creator(g, 0, 0)
routes = graph_brute_force(g, [])

i = 0
max_sum = 0
max_path = []

while(i+n < len(routes)):
    path = routes[i:i+n]
    path_sum = sum(path)
    if path_sum > max_sum:
        max_sum = path_sum
        max_path = path
    i += n

print max_path
print max_sum
