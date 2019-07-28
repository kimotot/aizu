class Node:
    def __init__(self, data=None, priority=None):
        self.data = data
        self.priority = priority
        self.left_node = None
        self.right_node = None


def _find(node, x):
    # nodeが空になるまで、検索を再帰的に行う
    while node is not None:
        if x == node.data:
            return node
        elif x < node.data:
            return _find(node.left_node, x)
        else:
            return _find(node.right_node, x)

    # ここまでくるのは、木が空か、検索データが見つからなかった場合
    return None


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


def _find_min(node):
    """
    nodeで指定された部分木の中から最小値を求める

    Parameters
    ----------
    node : Node
        検索対象となる部分木のルートを指す変数

    Returns
    -------
    Node.data : int
        最小値データ
    """
    if node is None:
        return None

    # 左の子がいないなら、nodeの値が最小値
    elif node.left_node is None:
        return node.data

    # 左の子がいるなら、その先を再帰的に探索
    else:
        return _find_min(node.left_node)


def _delete_min(node):
    if node is None:
        return None

    # 左の子がいないとき、今のノードが最小値。なので、それを削除した部分木は、すなわち右部分木になる
    elif node.left_node is None:
        return node.right_node

    # 左の子がいるときは、左の子の先を再帰的に探索して最小値を削除。戻り値である削除済部分木をnodeの左の子とする
    # また、呼び出し元への戻値はnodeを根とする削除済部分木なので、nodeを返すこととなる。
    else:
        node.left_node = _delete_min(node.left_node)
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


def _traverse_pre(node):
    if node is not None:
        yield node.data
        for x in _traverse_pre(node.left_node):
            yield x

        for x in _traverse_pre(node.right_node):
            yield x


def _traverse_in(node):
    if node is not None:
        for x in _traverse_in(node.left_node):
            yield x

        yield node.data

        for x in _traverse_in(node.right_node):
            yield x


def _traverse_post(node):
    if node is not None:
        for x in _traverse_post(node.left_node):
            yield x

        for x in _traverse_post(node.right_node):
            yield x

        yield node.data


def _print_bt(node, x=0):
    if node is not None:
        _print_bt(node.left_node, x + 1)
        print('    ' * x, node.data)
        _print_bt(node.right_node, x + 1)


# 表示
def _print_treap(node, x=0):
    if node is not None:
        _print_treap(node.left_node, x + 1)
        print("    " * x, node.data, node.priority)
        _print_treap(node.right_node, x + 1)



class Treap:
    def __init__(self):
        self.root = None

    # 探索
    def find(self, x):
        return _find(self.root, x) is not None

    # 挿入
    def insert(self, x, p):
        self.root = _insert(self.root, x, p)

    # 削除
    def delete(self, x):
        self.root = _delete(self.root, x)

    # 巡回
    def traverse(self, t="in"):
        if t == "pre":
            func = _traverse_pre
        elif t == "in":
            func = _traverse_in
        elif t == "post":
            func = _traverse_post
        else:
            return

        for x in func(self.root):
            yield x

    # リスト表示(inorder traverseで)
    def show_list(self, t="in"):
        print([x for x in self.traverse(t)])

    def print_treap(self):
        _print_treap(self.root)


if __name__ == "__main__":
    treap = Treap()

    n = int(input())
    for _ in range(n):
        operation = input().split()
        if operation[0] == "insert":
            treap.insert(int(operation[1]), int(operation[2]))
        elif operation[0] == "delete":
            treap.delete(int(operation[1]))
        elif operation[0] == "find":
            if treap.find(int(operation[1])):
                print("yes")
            else:
                print("no")
        else:
            str_in = ""
            for x in treap.traverse(t = "in"):
                str_in += " {0:d}".format(x)

            str_pre = ""
            for x in treap.traverse(t = "pre"):
                str_pre += " {0:d}".format(x)

            print(str_in)
            print(str_pre)

