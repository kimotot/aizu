INF = 2 ** 31 - 1

class RSQ:

    def __init__(self, n, N):
        self.n = n

        self.nodes = [0] * (N * 2 - 1)
        self.N = N

    def add(self, i, x):
        i = i + self.N - 1
        self.nodes[i] += x

        while i > 0:
            i = (i - 1) // 2
            self.nodes[i] += x

    def _getSum(self, s, t, i, l, r):
        if s <= l and r <= t:
            return self.nodes[i]
        elif t <= l or r <= s:
            return 0
        else:
            m = (l + r) // 2
            return self._getSum(s, t, i * 2 + 1, l, m) + self._getSum(s, t, i * 2 + 2, m, r)

    def getSum(self, s, t):
        return self._getSum(s, t + 1, 0, 0, self.N)


if __name__ == "__main__":
    n, q = map(int, input().split())
    N = 1
    while n > N:
        N *= 2
    rmq = RSQ(n, N)

    for _ in range(q):
        com, *arg = [int(x) for x in input().split()]
        if com == 0:        # update
            rmq.add(arg[0] - 1, arg[1])
        else:
            print(rmq.getSum(arg[0] - 1, arg[1] - 1))
