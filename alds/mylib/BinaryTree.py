import random


class Node:
    def __init__(self, data=None):
        self.data = data
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


def _insert(node, x):
    # nodeが空なら、xをデータとする新しいNodeオブジェクを作って返す
    if node is None:
        return Node(x)
    else:
        if x < node.data:       # 左部分木にデータを挿入
            node.left_node = _insert(node.left_node, x)
        else:                   # 右部分木にデータを挿入
            node.right_node = _insert(node.right_node, x)

        # 戻り値として、挿入済の部分木を返す
        return node


def _find_min(node):
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


def _delete(node, x):
    # nodeを根とする部分木から、xをデータとして持つノードを見つける（削除対象のノードを見つける）
    r = _find(node, x)

    # 削除要素が見つからなければ、削除対象の部分木をそのまま返す
    if r is None:
        return node

    # 右の子がいなければ、左の子を返す
    elif r.right_node is None:
        return r.left_node

    # 左の子がいなけば、右部分木を返す
    elif r.left_node is None:
        return r.right_node

    # 上記二つの判定文に、両方の子がNoneだった場合が含まれる

    else:
        # 右部分木から最小値を見つけて根のデータを上書き。右部分木から最小値のノードを削除
        r.data = _find_min(r.right_node)
        r.right_node = _delete_min(r.right_node)
        return r


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



class BinaryTree:
    def __init__(self):
        self.root = None

    # 探索
    def find(self, x):
        return _find(self.root, x) is not None

    # 挿入
    def insert(self, x):
        self.root = _insert(self.root, x)

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


    def print_bt(self):
        _print_bt(self.root)


if __name__ == "__main__":
    tree = BinaryTree()
    for _ in range(20):
        tree.insert(random.randint(0, 1000))
    tree.print_bt()


