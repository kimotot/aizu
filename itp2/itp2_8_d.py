from bisect import bisect_left, bisect_right, insort_left, insort_right

class Map:

    def __init__(self):
        self.d = dict()
        self.bl = []

    def insert(self, key, x):
        if key in self.d:
            self.d[key].append(x)
        else:
            self.d[key] = [x]
            insort_left(self.bl, key)

    def get(self, key):
        global fw
        if key in self.d and self.d[key] != []:
            for x in self.d[key]:
                # print(x)
                fw.write(str(x) + "\n")

    def delete(self, key):
        self.d[key] = []

    def dump(self, L, R):
        l = bisect_left(self.bl, L)
        r = bisect_right(self.bl, R)
        for i in range(l, r):
            key = self.bl[i]
            vl = self.d[key]
            if len(vl) > 0:
                for v in vl:
                    # print(key, v)
                    fw.write(key + " " + str(v) + "\n")


path = "C:\\Users\\1011249\\Desktop\\in23.txt"
path_w = "C:\\Users\\1011249\\Desktop\\in23o.txt"

fw = open(path_w, mode="w")

with open(path) as f:
    q = int(f.readline())
    m = Map()
    for al in f:
        a = al.split()
        if a[0] == "0":
            m.insert(a[1], int(a[2]))
        elif a[0] == "1":
            m.get(a[1])
        elif a[0] == "2":
            m.delete(a[1])
        else:
            m.dump(a[1], a[2])
