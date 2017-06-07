import math

class point:

    def __init__(self, p):
        self._x = p[0]
        self._y = p[1]

    def disp(self):
        print("{0:f} {1:f}".format(self._x, self._y))

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


def get_s(p1, p2):
    p = point((p1.x/3*2 + p2.x/3, p1.y/3*2 + p2.y/3))
    return p


def get_t(p1, p2):
    p = point((p1.x/3 + p2.x/3*2, p1.y/3 + p2.y/3*2))
    return p


def get_u(s, t):
    x = (t.x - s.x)*math.cos(math.radians(60)) - (t.y - s.y)*math.sin(math.radians(60)) + s.x
    y = (t.x - s.x)*math.sin(math.radians(60)) + (t.y - s.y)*math.cos(math.radians(60)) + s.y
    return point((x, y))


def kock(n, p1, p2):
    if n == 0:
        return
    else:
        s = get_s(p1, p2)
        t = get_t(p1, p2)
        u = get_u(s, t)

        kock(n-1, p1, s)
        s.disp()
        kock(n-1, s, u)
        u.disp()
        kock(n-1, u, t)
        t.disp()
        kock(n-1, t, p2)

        return


if __name__ == '__main__':

    n = int(input())

    p1 = point((0, 0))
    p2 = point((100, 0))

    p1.disp()
    kock(n, p1, p2)
    p2.disp()


