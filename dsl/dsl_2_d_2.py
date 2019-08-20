INF = 2 ** 31 - 1


class RUQ:

    class Node:

        def __init__(self):
            self.time = -1
            self.value = INF

    def __init__(self, n):
        N = 1
        while n > N:
            N = N * 2
        self.A = [RUQ.Node() for _ in range(2 * N - 1)]
        self.n = n
        self.N = N

    def _update(self, s, t, x, time, nid, left, right):
        if s <= left < right <= t:
            self.A[nid].time = time
            self.A[nid].value = x
            return
        elif t <= left or right <= s:
            return
        else:
            middle = (left + right) // 2
            self._update(s, t, x, time, 2 * nid + 1, left, middle)
            self._update(s, t, x, time, 2 * nid + 2, middle, right)

    def update(self, s, t, x, time):
        self._update(s, t + 1, x, time, 0, 0, self.N)

    def _find(self, i):
        if i > 0:
            pi = (i + 1) // 2 - 1
            time, value = self._find(pi)
            if time > self.A[i].time:
                self.A[i].time = time
                self.A[i].value = value

        return self.A[i].time, self.A[i].value

    def find(self, i):
        _, value = self._find(i + self.N - 1)
        print(value)


if __name__ == "__main__":
    n, q = map(int, input().split())
    ruq = RUQ(n)
    for i in range(q):
        inst, *args = [int(x) for x in input().split()]
        if inst == 0:
            ruq.update(*args, i)
        else:
            ruq.find(*args)