class Point:

    def __init__(self, n, x, y):
        self.n = n
        self.x = x
        self.y = y

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

            self.ps[left:right] = sorted(self.ps[left:right], key=lambda x: x[key])
            middle = (left + right) // 2
            node = Node(middle)
            node.left = self.make2dtree(left, middle, depth + 1)
            node.right = self.make2dtree(middle + 1, right, depth + 1)
            return node

    def find(self, pidx, sx, tx, sy, ty, depth):
        ans = []
        if sx <= self.ps[pidx][1] <= tx and sy <= self.ps[pidx][2] <= ty:
            ans = [self.ps[pidx]]
            if depth % 2 == 0:
                if tx < self.ps[pidx][1]:
                    ans.append(self.find())
            else:
                key = 2

