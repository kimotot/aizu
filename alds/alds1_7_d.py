class Node:

    def __init__(self, n):
        self.id = n
        self.left = None
        self.right = None

class BTree:

    def __init__(self, n):
        self.n = n
        self.nodes = [Node(i) for i in range(n + 1)]

    def make_tree(self, preorder, inorder):
        if preorder:
            root = preorder[0]
            i_root = inorder.index(root)
            inorder_left = inorder[:i_root]
            inorder_right = inorder[i_root + 1:]
            leftn = len(inorder_left)
            preorder_left = preorder[1:leftn + 1]
            preorder_right = preorder[leftn + 1:]

            self.nodes[root].left = self.make_tree(preorder_left, inorder_left)
            self.nodes[root].right = self.make_tree(preorder_right, inorder_right)

            return root

        else:
            return -1

    def disp_postorder(self, root, result):
        node = self.nodes[root]
        if node.left != -1:
            self.disp_postorder(node.left, result)
        if node.right != -1:
            self.disp_postorder(node.right, result)
        result.append(root)
        return result

if __name__ == '__main__':

    n = int(input())
    btree = BTree(n)

    preorder = [int(x) for x in input().split()]
    inorder = [int(x) for x in input().split()]

    btree.make_tree(preorder, inorder)

    result = btree.disp_postorder(preorder[0], [])
    print(" ".join([str(x) for x in result]))

