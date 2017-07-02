import heapq

class Node:

    def __init__(self, idx):
        self.idx = idx
        self.selected = False
        self.cost = 1000000
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
        self.nodes[s].cost = 0

    def update(self):
        pq = PQ()
        for node in self.nodes:
            pq.push(node)

        while True:
            try:
                u_idx = pq.pop()
                unode = self.nodes[u_idx]
                for (v, d) in unode.next:
                    vnode = self.nodes[v]
                    if vnode.cost > unode.cost + d:
                        vnode.cost = unode.cost + d
                        vnode.prev = unode.idx
                        pq.push(vnode)
            except KeyError:
                break

class PQ:

    def __init__(self):
        self.pq = []
        self.entry_finder = {}

    def push(self, node: Node):
        if node.idx in self.entry_finder:
            self.remove(node.idx)
        entry = [node.cost, node.idx]
        self.entry_finder[node.idx] = entry
        heapq.heappush(self.pq, entry)

    def remove(self, idx):
        entry = self.entry_finder.pop(idx)
        entry[-1] = -1

    def pop(self):
        while self.pq:
            (cost, idx) = heapq.heappop(self.pq)
            if idx != -1:
                del self.entry_finder[idx]
                return idx
        raise KeyError("pop form an empty priority queue")

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
