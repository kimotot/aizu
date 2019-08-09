MASK = 2 ** 64 - 1

class Bitflag:

    def __init__(self):
        self.v = 0

    def test(self, i):
        mask = 1 << i
        if self.v & mask > 0:
            return 1
        else:
            return 0

    def set(self, m):
        self.v = self.v | m

    def clear(self, m):
        m = ~m & MASK
        self.v = self.v & m

    def flip(self, m):
        self.v = self.v ^ m

    def all(self, m):
        if self.v & m == m:
            return 1
        else:
            return 0

    def any(self, m):
        if self.v & m > 0:
            return 1
        else:
            return 0

    def none(self, m):
        if self.v & m == 0:
            return 1
        else:
            return 0

    def count(self, m):
        t = self.v & m
        c = 0
        i = 0
        while i < 64:
            if t & (1 << i) > 0:
                c += 1
            i += 1
        return c

    def val(self, m):
        return self.v & m


n = int(input())
masks = []
for _ in range(n):
    k, *b = [int(x) for x in input().split()]
    t = 0
    for i in b:
        t = t | (1 << i)
    masks.append(t)

q = int(input())
b = Bitflag()
for _ in range(q):
    inst, m = [int(x) for x in input().split()]
    if inst == 0:
        print(b.test(m))
    elif inst == 1:
        b.set(masks[m])
    elif inst == 2:
        b.clear(masks[m])
    elif inst == 3:
        b.flip(masks[m])
    elif inst == 4:
        print(b.all(masks[m]))
    elif inst == 5:
        print(b.any(masks[m]))
    elif inst == 6:
        print(b.none(masks[m]))
    elif inst == 7:
        print(b.count(masks[m]))
    else:
        print(b.val(masks[m]))
