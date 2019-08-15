import datetime
from operator import itemgetter
import sys

input = sys.stdin.readline


class Node:

    def __init__(self, idx):
        self.idx = idx
        self.left = None
        self.right = None


class KDtree:

    def __init__(self, a):
        self.ps = a[:]
        self.root = self.make2dtree(0, len(self.ps), 0)

    def make2dtree(self, left, right, depth):
        if left >= right:
            return None
        else:
            if depth % 2 == 0:
                key = 1
            else:
                key = 2

            self.ps[left:right] = sorted(self.ps[left:right], key=itemgetter(key))
            middle = (left + right) // 2
            node = Node(middle)
            node.left = self.make2dtree(left, middle, depth + 1)
            node.right = self.make2dtree(middle + 1, right, depth + 1)
            return node

    def find(self, node, sx, tx, sy, ty, depth):
        ans = []
        x = self.ps[node.idx][1]
        y = self.ps[node.idx][2]
        if sx <= x <= tx and sy <= y <= ty:
            ans = [self.ps[node.idx]]

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

        ans.sort(key=lambda x: x[0])
        for p in ans:
            print(p[0])
        print("")


if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(n):
        a.append(tuple([i] + [int(x) for x in input().split()]))

    q = int(input())
    kd = KDtree(a)
    for _ in range(q):
        args = [int(x) for x in input().split()]
        kd.display(*args)

# if __name__ == "__main__":
#     f = open("C:\\Users\\1011249\\Desktop\\in13.txt", "r")
#     n = int(f.readline())
#     a = []
#
#     start = datetime.datetime.now()
#
#     for i in range(n):
#         a.append(tuple([i] + [int(x) for x in f.readline().split()]))
#
#     rap1 = datetime.datetime.now()
#
#     q = int(f.readline())
#     kd = KDtree(a)
#
#     rap2 = datetime.datetime.now()
#
#     for _ in range(q):
#         args = [int(x) for x in f.readline().split()]
#         kd.display(*args)
#
#
#     print(start)
#     print(rap1)
#     print(rap2)
#     print(datetime.datetime.now())
