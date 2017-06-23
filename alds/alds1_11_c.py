class Node:

    def __init__(self, n, l):
        self.n = n
        self.next_list = l
        self.depth = -1
        self.visited = False

    def disp(self):
        print("{0} {1}".format(self.n, self.depth))

def bfs(nodes, s_list, d):
    next_node = set()
    for n in s_list:
        if nodes[n].visited:
            pass
        else:
            nodes[n].visited = True
            nodes[n].depth = d
            for s in nodes[n].next_list:
                if nodes[s].visited is False:
                    next_node.add(s)

    if next_node:
        bfs(nodes, next_node, d+1)


def decode():
    nodes = {}
    n = int(input())
    for _ in range(n):
        al = [int(x) for x in input().split()]
        nodes[al[0]] = Node(al[0], al[2:])
    return n, nodes


if __name__ == '__main__':
    n, nodes = decode()
    bfs(nodes, [1], 0)

    for i in range(1, n+1):
        nodes[i].disp()
