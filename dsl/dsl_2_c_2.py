import datetime
from operator import itemgetter
import sys

input = sys.stdin.readline


class Point:

    def __init__(self, n, x, y):
        self.n = n
        self.x = x
        self.y = y

class Node:

    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None


class KDtree:

    def __init__(self, pl):
        self.root = self.make2dtree(pl, 0)

    def make2dtree(self, pl, depth):
        if len(pl) == 0:
            return None
        else:
            if depth % 2 == 0:
                key = 1
            else:
                key = 2

            pl.sort(key=itemgetter(key))
            middle = len(pl) // 2
            point = Point(*pl[middle])
            node = Node(point)
            node.left = self.make2dtree(pl[:middle], depth + 1)
            node.right = self.make2dtree(pl[middle + 1:], depth + 1)
            return node

    def find(self, node, sx, tx, sy, ty, depth):
        ans = []
        x = node.point.x
        y = node.point.y
        if sx <= x <= tx and sy <= y <= ty:
            ans = [node.point.n]

        if depth % 2 == 0:
            if sx < x and node.left is not None:
                ans += self.find(node.left, sx, tx, sy, ty, depth + 1)
            if x < tx and node.right is not None:
                ans += self.find(node.right, sx, tx, sy, ty, depth + 1)
        else:
            if sy < y and node.left is not None:
                ans += self.find(node.left, sx, tx, sy, ty, depth + 1)
            if y < ty and node.right is not None:
                ans += self.find(node.right, sx, tx, sy, ty, depth + 1)
        return ans

    def display(self, sx, tx, sy, ty):
        ans = self.find(self.root, sx, tx, sy, ty, 0)

        ans.sort()
        for p in ans:
            print(p)
        print("")


# if __name__ == "__main__":
#     n = int(input())
#     a = []
#     for i in range(n):
#         a.append(tuple([i] + [int(x) for x in input().split()]))
#
#     q = int(input())
#     kd = kdtree(a)
#     for _ in range(q):
#         args = [int(x) for x in input().split()]
#         kd.display(*args)

if __name__ == "__main__":
    f = open("C:\\Users\\1011249\\Desktop\\in13.txt", "r")
    n = int(f.readline())
    a = []

    start = datetime.datetime.now()
    print(start)

    for i in range(n):
        a.append(tuple([i] + [int(x) for x in f.readline().split()]))

    rap1 = datetime.datetime.now()
    print(rap1)

    q = int(f.readline())
    kd = KDtree(a)

    rap2 = datetime.datetime.now()
    print(rap2)

    for _ in range(q):
        args = [int(x) for x in f.readline().split()]
        kd.display(*args)


    print(start)
    print(rap1)
    print(rap2)
    print(datetime.datetime.now())
