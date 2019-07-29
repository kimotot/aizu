from collections import deque


class Deque:

    def __init__(self):
        self.q = deque()

    def push(self, d, x):
        if d == 0:
            self.q.appendleft(x)
        else:
            self.q.append(x)

    def randomAccess(self, p):
        print(self.q[p])

    def pop(self, d):
        if d == 0:
            self.q.popleft()
        else:
            self.q.pop()


if __name__ == "__main__":
    n = int(input())
    dq = Deque()

    for _ in range(n):
        query = input()

        if query[0] == "0":
            dq.push(*[int(x) for x in query[2:].split()])
        elif query[0] == "1":
            dq.randomAccess(int(query[2:]))
        else:
            dq.pop(int(query[2:]))