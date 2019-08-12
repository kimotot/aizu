INF = 2 ** 31 - 1

class RMQ:

    def __init__(self, n, N):
        self.n = n

        self.nodes = [INF] * (N * 2 - 1)
        self.N = N

    def update(self, i, x):
        i = i + self.N - 1
        self.nodes[i] = x

        while i > 0:
            i = (i - 1) // 2
            self.nodes[i] = min(self.nodes[i * 2 + 1], self.nodes[i * 2 + 2])

    def _find(self, s, t, i, l, r):
        if s <= l and r <= t:
            return self.nodes[i]
        elif t <= l or r <= s:
            return INF
        else:
            m = (l + r) // 2
            return min(self._find(s, t, i * 2 + 1, l, m), self._find(s, t, i * 2 + 2, m, r))

    def find(self, s, t):
        return self._find(s, t + 1, 0, 0, self.N)


if __name__ == "__main__":
    n, q = map(int, input().split())
    N = 1
    while n > N:
        N *= 2
    rmq = RMQ(n, N)

    for _ in range(q):
        com, *arg = [int(x) for x in input().split()]
        if com == 0:        # update
            rmq.update(*arg)
        else:
            print(rmq.find(*arg))
