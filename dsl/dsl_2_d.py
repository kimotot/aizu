import sys
input = sys.stdin.readline

INF = 2 ** 31 - 1


class RUQ:

    def __init__(self, n):
        self.a = [INF] * n

    def update(self, s, t, x):
        if s > t:
            tmp = s
            s = t
            t = tmp

        for i in range(s, t + 1):
            self.a[i] = x

    def find(self, i):
        print(self.a[i])


if __name__ == "__main__":
    n, q = map(int, input().split())
    ruq = RUQ(n)
    for _ in range(q):
        inst, *args = [int(x) for x in input().split()]
        if inst == 0:
            ruq.update(*args)
        else:
            ruq.find(*args)