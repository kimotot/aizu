class Node:

    def __init__(self, idx):
        self.idx = idx
        self.selected = False
        self.cost = None
        self.prev = None
        self.next = []

    def set_next(self, args):
        for i in range(args[0]):
            self.next.append((args[i*2+1], args[i*2+2]))

    def debug_disp(self):
        print(self.idx)
        print(self.selected)
        print(self.cost)
        print(self.next)
        print("")

    def disp(self):
        print("{0} {1}".format(self.idx, self.cost))

class Dijkstra:

    def __init__(self, n):
        self.n = n
        self.nodes = [Node(i) for i in range(n)]

    def initialize(self, s):
        self.nodes[s].selected = False
        self.nodes[s].cost = 0

    def update(self):
        ns = list(filter(lambda n: not n.selected and n.cost is not None, self.nodes))

        while ns:
            unode = min(ns, key=lambda n: n.cost)
            unode.selected = True
            for (v, d) in unode.next:
                vnode = self.nodes[v]
                if vnode.cost is None or vnode.cost > unode.cost + d:
                    vnode.cost = unode.cost + d
                    vnode.prev = unode.idx
            ns = list(filter(lambda n: not n.selected and n.cost is not None, self.nodes))


def decode():
    n = int(input())
    tree = Dijkstra(n)

    for _ in range(n):
        al = [int(x) for x in input().split()]
        tree.nodes[al[0]].set_next(al[1:])

    return n, tree


if __name__ == '__main__':

    n, tree = decode()

    tree.initialize(0)
    tree.update()

    for node in tree.nodes:
        node.disp()
