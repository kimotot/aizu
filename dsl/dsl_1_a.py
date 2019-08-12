class Node:

    def __init__(self, n):
        self.n = n
        self.parent = n
        self.rank = 0


class UFTree:

    def __init__(self, m):
        self.m = m
        self.Nodes = [Node(i) for i in range(m)]

    def get_parent(self, n):
        if self.Nodes[n].parent == n:
            return n
        else:
            self.Nodes[n].parent = self.get_parent(self.Nodes[n].parent)
            return self.Nodes[n].parent

    def unite(self, x, y):
        x_parent = self.get_parent(x)
        y_parent = self.get_parent(y)

        if x_parent != y_parent:
            if self.Nodes[x_parent].rank > self.Nodes[y_parent].rank:
                self.Nodes[y_parent].parent = x_parent
            elif self.Nodes[x_parent].rank == self.Nodes[y_parent].rank:
                self.Nodes[y_parent].parent = x_parent
                self.Nodes[x_parent].rank += 1
            else:
                self.Nodes[x_parent].parent = y_parent

    def same(self, x, y):
        if self.get_parent(x) == self.get_parent(y):
            print(1)
        else:
            print(0)


def main():
    [n, q] = [int(x) for x in input().split()]
    uft = UFTree(n)

    for _ in range(q):
        aline = [int(x) for x in input().split()]
        if aline[0] == 0:       # unite
            uft.unite(*aline[1:])
        else:                   # same
            uft.same(*aline[1:])

main()


