INF = 2 ** 31 - 1


class RMUQ:

    class Node:

        def __init__(self):
            self.time = -1
            self.v = INF
            self.min_v = INF

    def __init__(self, n):
        N = 1
        while n > N:
            N = N * 2
        self.A = [RMUQ.Node() for _ in range(2 * N - 1)]
        self.n = n
        self.N = N

    def _update(self, s, t, x, time, nid, left, right):
        if s <= left < right <= t:
            self.A[nid].time = time
            self.A[nid].v = x
            self.A[nid].min_v = x
            return x
        elif t <= left or right <= s:
            return self.A[nid].min_v
        else:
            middle = (left + right) // 2
            ml = self._update(s, t, x, time, 2 * nid + 1, left, middle)
            mr = self._update(s, t, x, time, 2 * nid + 2, middle, right)
            self.A[nid].min_v = min(ml, mr)
            return self.A[nid].min_v

    def update(self, s, t, x, time):
        self.A[0].min_v = self._update(s, t + 1, x, time, 0, 0, self.N)

    def _find(self, s, t, nid, left, right):
        if s <= left < right <= t:
            return self.A[nid].min_v

        if t <= left or right <= t:
            return self.A[nid].min_v

        middle = (left + right) // 2
        ml = self._find(s, t, 2 * nid + 1, left, middle)
        mr = self._find(s, t, 2 * nid + 2, middle, right)
        self.A[nid].min_v = min(ml, mr)
        return self.A[nid].min_v

    def find(self, s, t):
        print(self._find(s, t + 1, 0, 0, self.N))


if __name__ == "__main__":
    n, q = map(int, input().split())
    rmuq = RMUQ(n)
    for i in range(q):
        inst, *args = [int(x) for x in input().split()]
        if inst == 0:
            rmuq.update(*args, i)
        else:
            rmuq.find(*args)
