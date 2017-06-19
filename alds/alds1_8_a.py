class Node:

    def __init__(self, k):
        self.key = k
        self.parent = None
        self.left = None
        self.right = None

class BTree:

    def __init__(self):
        self.root = None

    def insert(self, z):
        y = None
        x = self.root

        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y

        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def print_inorder(self):

        def print_inorder_innner(root, result):
            if root.left is not None:
                print_inorder_innner(root.left, result)
            result.append(root.key)
            if root.right is not None:
                print_inorder_innner(root.right, result)
            return result

        result = print_inorder_innner(self.root, [])
        print(" " + " ".join([str(x) for x in result]))

    def print_preorder(self):

        def print_preorder_innner(root, result):
            result.append(root.key)

            if root.left is not None:
                print_preorder_innner(root.left, result)
            if root.right is not None:
                print_preorder_innner(root.right, result)
            return result

        result = print_preorder_innner(self.root, [])
        print(" " + " ".join([str(x) for x in result]))


if __name__ == '__main__':
    btree = BTree()

    n = int(input())
    for _ in range(n):
        al = input().split()
        if al[0] == "insert":
            btree.insert(Node(int(al[1])))
        else:
            btree.print_inorder()
            btree.print_preorder()