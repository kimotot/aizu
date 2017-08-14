class RMQ:

    def __init__(self, n):
        self.n = n
        self.ary = [(2**31) - 1] * n

    def update(self, i , x):
        self.ary[i] = x

    def find(self, s, t):
        return min(self.ary[s:t+1])

[n, q] = [int(x) for x in input().split()]
rmq = RMQ(n)

for _ in range(q):
    [c, x, y] = [int(z) for z in input().split()]

    if c == 0:      # update
        rmq.update(x, y)
    else:           # find
        print(rmq.find(x, y))
