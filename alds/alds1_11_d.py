from collections import deque

class Node:

    def __init__(self, n):
        self.n = n
        self.friends = set()
        self.group = None

    def add_friend(self, t):
        self.friends.add(t)

    def debug_print(self):
        print("ID = {0} , F = {1}".format(self.n, self.friends))


def decode():
    [n, m] = [int(x) for x in input().split()]
    nodes = [Node(i) for i in range(n)]

    for _ in range(m):
        [s, t] = [int(x) for x in input().split()]
        nodes[s].add_friend(t)
        nodes[t].add_friend(s)

    q = int(input())
    qs = []
    for _ in range(q):
        qs.append([int(x) for x in input().split()])

    return n, m, nodes, q, qs


def dfs(nodes, s, g):
    nodes[s].group = g
    for t in nodes[s].friends:
        if nodes[t].group is None:
            dfs(nodes, t, g)


def bfs(nodes, stack, g):
    while stack:
        node = stack.pop()
        nodes[node].group = g
        for n in nodes[node].friends:
            if nodes[n].group is None:
                stack.add(n)


def make_groups(nodes):
    g_num = 0
    for node in nodes:
        if node.group is None:
            g_num += 1
            bfs(nodes, {node.n}, g_num)


if __name__ == '__main__':
    n, m, nodes, q, qs = decode()

    make_groups(nodes)
    for [s, t] in qs:
        if nodes[s].group == nodes[t].group:
            print("yes")
        else:
            print("no")
