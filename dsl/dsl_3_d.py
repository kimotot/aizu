INF = 10 ** 9 + 1


class SEGT:

    def __init__(self, n, aa):
        N = 1
        while n > N:
            N *= 2
        self.A = [INF] * (2 * N - 1)
        self.n = n
        self.N = N

        for i in range(n):
            self.A[i + N - 1] = aa[i]

        for i in range(N - 2, -1, -1):
            self.A[i] = min(self.A[i * 2 + 1], self.A[i * 2 + 2])

    def _getmin(self, s, t, i, left, right):
        if s <= left < right <= t:
            return self.A[i]

        if t <= left or right <= s:
            return INF

        middle = (left + right) // 2
        return min(self._getmin(s, t, i * 2 + 1, left, middle), self._getmin(s, t, i * 2 + 2, middle, right))

    def getmin(self, s, t):
        return self._getmin(s, t, 0, 0, self.N)


if __name__ == "__main__":
    n, l = map(int, input().split())
    aa = [int(x) for x in input().split()]

    segt = SEGT(n, aa)
    ans = []
    for s in range(n - l + 1):
        t = s + l
        ans.append(segt.getmin(s, t))

    print(" ".join([str(x) for x in ans]))
