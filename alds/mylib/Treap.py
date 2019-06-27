import random
from alds.mylib import BinaryTree as bt


class Node(bt.Node):
    def __init__(self, data=None, priority=None):
        bt.Node.__init__(self, data)
        self.priority = priority


# 特定のノードに対して右回転を行った部分木を返す関数
def _rotate_right(node):
    # 左の子が存在することを前提とし、右回転後の部分木を返す
    lnode = node.left_node
    node.left_node = lnode.right_node
    lnode.right_node = node
    return lnode


# 左回転
def _rotate_left(node):
    rnode = node.right_node
    node.right_node = rnode.left_node
    rnode.left_node = node
    return rnode


# 挿入
def _insert(node, x, p):
    # 挿入先が空だったら新たにNodeを作って返す
    if node is None:
        return Node(x, p)

    # 追加するデータと同じノードが存在したら追加をスキップ（重複データを許さない）
    if node.data == x:
        return node

    # 左部分木にデータを挿入
    if x < node.data:
        node.left_node = _insert(node.left_node, x, p)
        if node.left_node.priority > node.priority:     # 子の優先度が高ければ右回転
            node = _rotate_right(node)
    else:
        node.right_node = _insert(node.right_node, x, p)
        if node.right_node.priority > node.priority:    # 左回転
            node = _rotate_left(node)
    return node


# 削除
def _delete(node, x):
    if node is not None:
        if node.data == x:
            if node.left_node is None and node.right_node is None:
                return None
            elif node.left_node is None:
                return node.right_node
            elif node.right_node is None:
                return node.left_node
            else:
                if node.left_node.priority > node.right_node.priority:
                    node = _rotate_right(node)
                else:
                    node = _rotate_left(node)
                node = _delete(node, x)
        elif x < node.data:
            node.left_node = _delete(node.left_node, x)
        else:
            node.right_node = _delete(node.right_node, x)
    return node


# 表示
def _print_treap(node, x=0):
    if node is not None:
        _print_treap(node.left_node, x + 1)
        print("    " * x, node.data, node.priority)
        _print_treap(node.right_node, x + 1)


class Treap(bt.BinaryTree):
    def __init__(self):
        bt.BinaryTree.__init__(self)

    # 探索　親と同じ
    # def find(self, x):
    #   return _find(self.root, x) is not None

    # 挿入
    def insert(self, x, p):
        self.root = _insert(self.root, x, p)

    # 削除
    def delete(self, x):
        self.root = _delete(self.root, x)

    # 表示
    def print_treap(self):
        _print_treap(self.root)


if __name__ == "__main__":
    treap = Treap()
    for i in range(20):
        treap.insert(i, random.randint(0, 100))
    treap.print_treap()
    treap.show_list()

    treap.delete(10)
    treap.print_treap()
    treap.show_list()
