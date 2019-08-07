import random
MAXIMUM = 1000000000


class Node:

    def __init__(self, d=None):
        self.data = d
        self.left = None
        self.right = None
        self.priority = random.randint(0, MAXIMUM)
        self.sum = 1


def _find(node, x):
    # nodeが空になるまで、検索を再帰的に行う
    if node:
        if x == node.data:
            return node.sum
        elif x < node.data:
            return _find(node.left, x)
        else:
            return _find(node.right, x)

    # ここまでくるのは、木が空か、検索データが見つからなかった場合
    else:
        return 0


# 特定のノードに対して右回転を行った部分木を返す関数
def _rotate_right(node):
    # 左の子が存在することを前提とし、右回転後の部分木を返す
    lnode = node.left
    node.left = lnode.right
    lnode.right = node
    return lnode


# 左回転
def _rotate_left(node):
    rnode = node.right
    node.right = rnode.left
    rnode.left = node
    return rnode


# 挿入
def _insert(node, x):
    # 挿入先が空だったら新たにNodeを作って返す
    if node is None:
        return Node(x)

    # 追加するデータと同じノードが存在したら
    if node.data == x:
        node.sum += 1
        return node

    # 左部分木にデータを挿入
    if x < node.data:
        node.left = _insert(node.left, x)
        if node.left.priority > node.priority:     # 子の優先度が高ければ右回転
            node = _rotate_right(node)
    else:
        node.right = _insert(node.right, x)
        if node.right.priority > node.priority:    # 左回転
            node = _rotate_left(node)
    return node


# 削除
def _delete(node, x):
    if node is not None:
        if node.data == x:
            if node.left is None and node.right is None:
                return None, node.sum
            elif node.left is None:
                return node.right, node.sum
            elif node.right is None:
                return node.left, node.sum
            else:
                if node.left.priority > node.right.priority:
                    node = _rotate_right(node)
                else:
                    node = _rotate_left(node)
                node, c = _delete(node, x)
        elif x < node.data:
            node.left, c = _delete(node.left, x)
        else:
            node.right, c = _delete(node.right, x)
        return node, c
    else:
        return node, 0


def _dump(node, l, r):
    if node is None:
        pass
    elif node.data < l:
        _dump(node.right, l, r)
    elif l <= node.data <= r:
        _dump(node.left, l, r)
        for _ in range(node.sum):
            print(node.data)
        _dump(node.right, l, r)
    elif node.data > r:
        _dump(node.left, l, r)
    return

def _debug(node, depth):
    if node:
        _debug(node.left, depth + 1)
        print("  " * depth, node.data)
        _debug(node.right, depth + 1)


class Set:
    def __init__(self):
        self.root = None
        self.count = 0

    # 探索
    def find(self, x):
        print(_find(self.root, x))

    # 挿入
    def insert(self, x):
        self.root = _insert(self.root, x)
        self.count += 1
        print(self.count)

    # 削除
    def delete(self, x):
        self.root, c = _delete(self.root, x)
        self.count -= c

    # 範囲表示
    def dump(self, l, r):
        _dump(self.root, l, r)

    def debug(self):
        print("-----")
        _debug(self.root, 0)
        print("*****")


s = Set()
n = int(input())
for _ in range(n):
    q, *a = [int(x) for x in input().split()]
    if q == 0:
        s.insert(*a)
    elif q == 1:
        s.find(*a)
    elif q == 2:
        s.delete(*a)
    else:
        s.dump(*a)
