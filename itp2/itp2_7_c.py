import random
MAXIMUM = 1000000000


class Node:

    def __init__(self, d=None):
        self.data = d
        self.left = None
        self.right = None
        self.priority = random.randint(0, MAXIMUM)


def _find(node, x):
    # nodeが空になるまで、検索を再帰的に行う
    while node:
        if x == node.data:
            return node
        elif x < node.data:
            node = node.left
        else:
            node = node.right

    # ここまでくるのは、木が空か、検索データが見つからなかった場合
    return None


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
        return Node(x), True

    # 追加するデータと同じノードが存在したら追加をスキップ（重複データを許さない）
    if node.data == x:
        return node, False

    # 左部分木にデータを挿入
    if x < node.data:
        node.left, f = _insert(node.left, x)
        if node.left.priority > node.priority:     # 子の優先度が高ければ右回転
            node = _rotate_right(node)
    else:
        node.right, f = _insert(node.right, x)
        if node.right.priority > node.priority:    # 左回転
            node = _rotate_left(node)
    return node, f


# 削除
def _delete(node, x):
    if node is not None:
        if node.data == x:
            if node.left is None and node.right is None:
                return None, True
            elif node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True
            else:
                if node.left.priority > node.right.priority:
                    node = _rotate_right(node)
                else:
                    node = _rotate_left(node)
                node, f = _delete(node, x)
        elif x < node.data:
            node.left, f = _delete(node.left, x)
        else:
            node.right, f = _delete(node.right, x)
        return node, f
    else:
        return node, False


def _dump(node, l, r):
    if node is None:
        return
    elif node.data < l:
        _dump(node.right, l, r)
    elif l <= node.data <= r:
        _dump(node.left, l, node.data - 1)
        print(node.data)
        _dump(node.right, node.data + 1, r)
    elif node.data > r:
        _dump(node.left, l, r)


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
        if _find(self.root, x):
            print(1)
        else:
            print(0)

    # 挿入
    def insert(self, x):
        self.root, f = _insert(self.root, x)
        if f:
            self.count += 1
        print(self.count)

    # 削除
    def delete(self, x):
        self.root, f = _delete(self.root, x)
        if f:
            self.count -= 1

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
