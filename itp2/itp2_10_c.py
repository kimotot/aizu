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

    def set(self, i):
        mask = 1 << i
        self.v = self.v | mask

    def clear(self, i):
        mask = MASK ^ (1 << i)
        self.v = self.v & mask

    def flip(self, i):
        if self.test(i):
            self.clear(i)
        else:
            self.set(i)

    def all(self):
        if self.v == MASK:
            return 1
        else:
            return 0

    def any(self):
        i = 0
        while i < 64:
            if self.test(i):
                return 1
            else:
                i += 1
        return 0

    def none(self):
        if self.v == 0:
            return 1
        else:
            return 0

    def count(self):
        c = 0
        i = 0
        while i < 64:
            if self.test(i):
                c += 1
            i += 1
        return c

    def val(self):
        return self.v


q = int(input())
b = Bitflag()
for _ in range(q):
    inst, *i = [int(x) for x in input().split()]
    if inst == 0:
        print(b.test(*i))
    elif inst == 1:
        b.set(*i)
    elif inst == 2:
        b.clear(*i)
    elif inst == 3:
        b.flip(*i)
    elif inst == 4:
        print(b.all())
    elif inst == 5:
        print(b.any())
    elif inst == 6:
        print(b.none())
    elif inst == 7:
        print(b.count())
    else:
        print(b.val())
