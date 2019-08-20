INF = 2 ** 31 - 1


class RAQ:

    def __init__(self, n):
        N = 1
        while n > N:
            N = N * 2
        self.A = [0] * (2 * N - 1)
        self.n = n
        self.N = N

    def _add(self, s, t, x, nid, left, right):
        if s <= left < right <= t:
            self.A[nid] += x
            return
        elif t <= left or right <= s:
            return
        else:
            middle = (left + right) // 2
            self._add(s, t, x, 2 * nid + 1, left, middle)
            self._add(s, t, x, 2 * nid + 2, middle, right)

    def add(self, s, t, x):
        self._add(s - 1, t, x, 0, 0, self.N)

    def _get(self, i):
        v = 0
        if i > 0:
            pi = (i + 1) // 2 - 1
            v = self._get(pi)

        return self.A[i] + v

    def get(self, i):
        value = self._get(i + self.N - 2)
        print(value)


if __name__ == "__main__":
    n, q = map(int, input().split())
    ruq = RAQ(n)
    for i in range(q):
        inst, *args = [int(x) for x in input().split()]
        if inst == 0:
            ruq.add(*args)
        else:
            ruq.get(*args)