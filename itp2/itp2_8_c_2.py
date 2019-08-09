from bisect import bisect_left, bisect_right, insort_left, insort_right

class Map:

    def __init__(self):
        self.d = dict()
        self.bl = []

    def insert(self, key, x):
        if key in self.d:
            self.d[key] = x
        else:
            self.d[key] = x
            insort_left(self.bl, key)

    def get(self, key):
        print(self.d.get(key, 0))

    def delete(self, key):
        self.d[key] = 0

    def dump(self, L, R):
        l = bisect_left(self.bl, L)
        r = bisect_right(self.bl, R)
        for i in range(l, r):
            k = self.bl[i]
            v = self.d[k]
            if v != 0:
                print(k, v)


q = int(input())
m = Map()
for _ in range(q):
    a = input().split()
    if a[0] == "0":
        m.insert(a[1], int(a[2]))
    elif a[0] == "1":
        m.get(a[1])
    elif a[0] == "2":
        m.delete(a[1])
    else:
        m.dump(a[1], a[2])
