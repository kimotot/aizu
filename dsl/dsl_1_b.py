class Node:

    def __init__(self, n):
        self.n = n
        self.parent = n
        self.rank = 0
        self.dif = 0


class UFTree:

    def __init__(self, m):
        self.m = m
        self.Nodes = [Node(i) for i in range(m)]

    def get_parent(self, n):
        if self.Nodes[n].parent == n:
            return n
        else:
            r = self.get_parent(self.Nodes[n].parent)
            self.Nodes[n].dif += self.Nodes[self.Nodes[n].parent].dif
            self.Nodes[n].parent = r
            return r

    def relate(self, x, y, z):
        x_parent = self.get_parent(x)
        y_parent = self.get_parent(y)
        w = z + self.Nodes[x].dif - self.Nodes[y].dif

        if x_parent != y_parent:
            if self.Nodes[x_parent].rank > self.Nodes[y_parent].rank:
                self.Nodes[y_parent].parent = x_parent
                self.Nodes[y_parent].dif = w
            elif self.Nodes[x_parent].rank == self.Nodes[y_parent].rank:
                self.Nodes[y_parent].parent = x_parent
                self.Nodes[y_parent].dif = w
                self.Nodes[x_parent].rank += 1
            else:
                self.Nodes[x_parent].parent = y_parent
                self.Nodes[x_parent].dif = -w

    def diff(self, x, y):
        if self.get_parent(x) == self.get_parent(y):
            return self.Nodes[y].dif - self.Nodes[x].dif
        else:
            return None


def main():
    [n, q] = [int(x) for x in input().split()]
    uft = UFTree(n)

    for _ in range(q):
        aline = [int(x) for x in input().split()]
        if aline[0] == 0:       # unite
            uft.relate(*aline[1:])
        else:                   # same
            res = uft.diff(*aline[1:])
            if res is not None:
                print(res)
            else:
                print("?")

main()


