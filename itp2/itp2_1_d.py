class Vector2:

    def __init__(self, n):
        self.n = n
        self.array = [[] for _ in range(n)]

    def pushBack(self, n, x):
        self.array[n].append(x)

    def dump(self, n):
        print(" ".join([str(x) for x in self.array[n]]))

    def cler(self, n):
        self.array[n].clear()


if __name__ == "__main__":
    n, q = [int(x) for x in input().split()]
    v = Vector2(n)
    for _ in range(q):
        query = input()
        order = int(query[0])
        if order == 0:
            t, x = [int(x) for x in query[2:].split()]
            v.pushBack(t, x)
        else:
            t = int(query[2:])
            if order == 1:
                v.dump(t)
            else:
                v.cler(t)
