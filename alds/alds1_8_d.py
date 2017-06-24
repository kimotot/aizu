LEFT = 0
RIGHT = 1

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

    def find(self, key):
        current = self.root
        while current is not None:
            if current.key == key:
                print("yes")
                return

            if key < current.key:
                current = current.left
            else:
                current = current.right

        print("no")
        return

    def find_successor(self, node):
        current = node.right

        while current.left is not None:
            current = current.left

        return current

    def delete(self, key):
        current = self.root
        parent = None
        parent_lr = None
        while current.key != key:
            if key < current.key:
                parent = current
                parent_lr = LEFT
                current = current.left
            else:
                parent = current
                parent_lr = RIGHT
                current = current.right

            if current is None:
                return None

        if current.left is None and current.right is None:
            if parent_lr == LEFT:
                parent.left = None
            else:
                parent.right = None

        elif current.left is None and current.right is not None:
            if parent_lr == LEFT:
                parent.left = current.right
            else:
                parent.right = current.right

        elif current.left is not None and current.right is None:
            if parent_lr == LEFT:
                parent.left = current.left
            else:
                parent.right = current.left

        else:
            successor = self.find_successor(current)
            new_key = successor.key
            self.delete(successor.key)
            current.key = new_key

        del current


    def print_inorder(self):

        def print_inorder_innner(root):
            if root.left is not None:
                print_inorder_innner(root.left)
            print(" {0}".format(root.key), end="")
            if root.right is not None:
                print_inorder_innner(root.right)

        print_inorder_innner(self.root)
        print("")

    def print_preorder(self):

        def print_preorder_innner(root):
            print(" {0}".format(root.key), end="")

            if root.left is not None:
                print_preorder_innner(root.left)
            if root.right is not None:
                print_preorder_innner(root.right)

        print_preorder_innner(self.root)
        print("")

    def debug_print(self):

        def debug_print_inner(root):
            if root.left is None:
                lstr = "None"
            else:
                lstr = "{0:4d}".format(root.left.key)

            if root.right is None:
                rstr = "None"
            else:
                rstr = "{0:4d}".format(root.right.key)

            print("{0:4d} : {1} , {2}".format(root.key, lstr, rstr))

            if root.left is not None:
                debug_print_inner(root.left)

            if root.right is not None:
                debug_print_inner(root.right)

        root = self.root
        debug_print_inner(root)


if __name__ == '__main__':
    btree = BTree()

    n = int(input())
    inst = []
    for _ in range(n):
        al = input().split()
        if al[0] == "print":
            inst.append(("print", 0))
        elif al[0] == "debug":
            inst.append(("debug", 0))
        else:
            inst.append((al[0], int(al[1])))

    for (i, k) in inst:

        if i == "insert":
            btree.insert(Node(k))
        elif i == "find":
            btree.find(k)
        elif i == "delete":
            btree.delete(k)
        elif i == "debug":
            btree.debug_print()
        else:
            btree.print_inorder()
            btree.print_preorder()