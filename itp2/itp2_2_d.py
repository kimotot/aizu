class Node:

    def __init__(self, value):
        self.v = value
        self.next = None


class Head:

    def __init__(self):
        self.root = None
        self.bottom = None


class Splice:

    def __init__(self, n):
        self.l = [Head() for _ in range(n)]

    def insert(self, t, x):
        if self.l[t].root is None:
            self.l[t].root = self.l[t].bottom = Node(x)
        else:
            new_node =Node(x)
            self.l[t].bottom.next = new_node
            self.l[t].bottom = new_node

    def dump(self, t):
        ans = []
        idx = self.l[t].root
        while idx is not None:
            ans.append(str(idx.v))
            idx = idx.next

        print(" ".join(ans))

    def splice(self, s, t):
        if self.l[t].root is None:
            self.l[t].root = self.l[s].root
            self.l[t].bottom = self.l[s].bottom
            self.l[s].root = self.l[s].bottom = None
        elif self.l[s].root is None:
            pass
        else:
            self.l[t].bottom.next = self.l[s].root
            self.l[t].bottom = self.l[s].bottom
            self.l[s].root = self.l[s].bottom = None


if __name__ == "__main__":

    n, q = [int(x) for x in input().split()]
    s = Splice(n)

    for _ in range(q):
        query = input()
        order = int(query[0])

        if order == 0:
            t, x = [int(x) for x in query[2:].split()]
            s.insert(t, x)
        elif order == 1:
            t = int(query[2:])
            s.dump(t)
        else:
            a1, a2 = [int(x) for x in query[2:].split()]
            s.splice(a1, a2)