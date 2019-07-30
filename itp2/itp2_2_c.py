import heapq

class PQueue:

    def __init__(self, n):
        self.queues = [[] for _ in range(n)]

    def insert(self, t, x):
        heapq.heappush(self.queues[t], -x)

    def getMax(self, t):
        if len(self.queues[t]) != 0:
            print(-self.queues[t][0])

    def deleteMax(self, t):
        if len(self.queues[t]) != 0:
            heapq.heappop(self.queues[t])


n, q = [int(x) for x in input().split()]
s = PQueue(n)

for _ in range(q):
    query = input()
    order = int(query[0])

    if order == 0:
        t, x = [int(x) for x in query[2:].split()]
        s.insert(t, x)
    elif order == 1:
        t = int(query[2:])
        s.getMax(t)
    else:
        t = int(query[2:])
        s.deleteMax(t)

