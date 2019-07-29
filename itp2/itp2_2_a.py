class Stack:

    def __init__(self, n):
        self.stacks = [[] for _ in range(n)]

    def push(self, t, x):
        self.stacks[t].append(x)

    def top(self, t):
        if len(self.stacks[t]) != 0:
            print(self.stacks[t][-1])

    def pop(self, t):
        if len(self.stacks[t]) != 0:
            self.stacks[t].pop()


n, q = [int(x) for x in input().split()]
s = Stack(n)

for _ in range(q):
    query = input()
    order = int(query[0])

    if order == 0:
        t, x = [int(x) for x in query[2:].split()]
        s.push(t, x)
    elif order == 1:
        t = int(query[2:])
        s.top(t)
    else:
        t = int(query[2:])
        s.pop(t)

