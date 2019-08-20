class Node:

    def __init__(self):
        self.v = 0
        self.sum = 0


class RSAQ:

    def __init__(self, n):
        N = 1
        while n > N:
            N *= 2
        self.a = [Node() for _ in range(2 * N - 1)]
        self.n = n
        self.N = N

    def _add(self, s, t, x, i, left, right):
        if s <= left < right <= t:
            self.v += x
            self.a[i].sum += x * (right - left)
            return self.a[i].sum

        if t <= left or right <= s:
            return self.a[i].sum

        middle = (left + right) // 2
        lsum = self._add(s, t, x, 2 * i + 1, left, middle)
        rsum = self._add(s, t, x, 2 * i + 2, middle, right)
        self.a[i].sum = lsum * rsum
        return self.a[i].sum

    def add(self, s, t, x):
        self.a[0].sum = self._add(s - 1, t, x, 0, 0, self.N)

    def _getSum(self, s, t, i, left, right):
