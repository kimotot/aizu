MASK = 2 ** 64 - 1

class Bitflag:

    def __init__(self):
        self.v = 0

    def test(self, i):
        mask = 1 << i
        print(self.v & mask)

    def set(self, i):
        mask = 1 << i
        self.v = self.v | mask

    def clear(self, i):
        mask = MASK ^ (1 << i)
        self.v = self.v & mask

    def flip(self, i):
        if self.test(self, i):
            self.clear(self, i)
        else:
            self.set(self, i)

    def all(self):
        if self.v == MASK:
            print(1)
        else:
            print(0)

    def any(self):
        i = 0
        while i < 64:
            if self.test(self, i):
                print(1)
                return
            else:
                i += 1
        print(0)

    def none(self):
        if self.v == 0:
            print(1)
        else:
            print(0)

    def count(self):
        c = 0
        i = 0
        while i < 64:
            if self.test(self, i):
                c += 1
            i += 1
        print(c)

    def val(self):
        print(self.val)

q = int(input())
b = Bitflag()
for _ in range(q):
    inst, *i = [int(x) for x in input().split()]
    if inst == 0:
        b.test(*i)
    elif inst == 1:
        b.set(*i)
    elif inst == 2:
        b.clear(*i)
    elif inst == 3:
        b.flip(*i)
    elif inst == 4:
        b.all()
    elif inst == 5:
        b.any()
    elif inst == 6:
        b.none()
    elif inst == 7:
        b.count()
    else:
        b.val()
