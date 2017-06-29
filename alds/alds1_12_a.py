class Node:

    def __init__(self, num):
        self.num = num
        self.parent = None
        self.rank = 0


class Tree:

    def __init__(self, n):
        self.n = n
        self.nodes = [Node(i) for i in range(n)]

    def find(self, x):
        if self.nodes[x].parent is None:
            return x
        else:
            self.nodes[x].parent = self.find(self.nodes[x].parent)
            return self.nodes[x].parent

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root != y_root:
            if self.nodes[x_root].rank > self.nodes[y_root].rank:
                self.nodes[y_root].parent = x_root
            elif self.nodes[x_root].rank < self.nodes[y_root].rank:
                self.nodes[x_root].parent = y_root
            else:
                self.nodes[y_root].parent = x_root
                self.nodes[x_root].rank += 1

    def isgroup(self, x, y):
        if self.find(x) == self.find(y):
            return True
        else:
            return False


def decode():
    n = int(input())
    es = []
    for i in range(n):
        al = [int(x) for x in input().split()]
        for j in range(i + 1, n):
            if al[j] != -1:
                es.append((i, j, al[j]))
    es.sort(key=lambda x: x[2])

    return n, es

if __name__ == '__main__':

    n, es = decode()

    tree = Tree(n)
    ans = 0

    for (x, y, v) in es:
        if tree.isgroup(x, y):
            pass
        else:
            ans += v
            tree.union(x, y)

    print(ans)
