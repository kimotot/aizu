from collections import deque

class Queue:

    def __init__(self, n):
        self.queues = [deque() for _ in range(n)]

    def enqueue(self, t, x):
        self.queues[t].append(x)

    def front(self, t):
        if len(self.queues[t]) != 0:
            print(self.queues[t][0])

    def dequeue(self, t):
        if len(self.queues[t]) != 0:
            self.queues[t].popleft()


n, q = [int(x) for x in input().split()]
s = Queue(n)

for _ in range(q):
    query = input()
    order = int(query[0])

    if order == 0:
        t, x = [int(x) for x in query[2:].split()]
        s.enqueue(t, x)
    elif order == 1:
        t = int(query[2:])
        s.front(t)
    else:
        t = int(query[2:])
        s.dequeue(t)

