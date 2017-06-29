class Node:

    def __init__(self, n):
        self.id = n
        self.parent = -1
        self.left = -1
        self.right = -1
        self.type = None
        self.depth = None
        self.height = None
        self.degree = None
        self.sibling = None


class BTree:

    def __init__(self, n):
        self.nodes = [Node(i) for i in range(n)]

    def add_children(self, node_id, l, r):
        if l != -1:
            self.nodes[node_id].left = l
            self.nodes[l].parent = node_id

        if r != -1:
            self.nodes[node_id].right = r
            self.nodes[r].parent = node_id

    def get_root(self):
        for node in self.nodes:
            if node.parent == -1:
                return node.id
        return -1

    def update_mytype_children(self, my_id, depth, sibling):
        mynode = self.nodes[my_id]
        mynode.depth = depth
        mynode.sibling = sibling
        deg = 0
        if mynode.left == mynode.right == -1:
            mynode.type = "leaf"
            mynode.degree = 0
        else:
            mynode.type = "internal node"
            if mynode.left != -1:
                deg += 1
                self.update_mytype_children(mynode.left, depth + 1, mynode.right)
            if mynode.right != -1:
                deg += 1
                self.update_mytype_children(mynode.right, depth + 1, mynode.left)
            mynode.degree = deg

    def update_type_depth(self):
        root = self.get_root()
        self.nodes[root].type = "root"
        self.nodes[root].depth = 0
        deg = 0
        if self.nodes[root].left != -1:
            deg += 1
            self.update_mytype_children(self.nodes[root].left, 1, self.nodes[root].right)
        if self.nodes[root].right != -1:
            deg += 1
            self.update_mytype_children(self.nodes[root].right, 1, self.nodes[root].left)

        self.nodes[root].degree = deg
        self.nodes[root].sibling = -1

    def get_myheight(self, my_id):
        l_height = r_height = 0
        if self.nodes[my_id].left != -1:
            l_height = self.get_myheight(self.nodes[my_id].left) + 1
        if self.nodes[my_id].right != -1:
            r_height = self.get_myheight(self.nodes[my_id].right) + 1

        self.nodes[my_id].height = max(l_height, r_height)
        return self.nodes[my_id].height

    def update_height(self):
        root = self.get_root()
        self.get_myheight(root)

    def disp(self):
        for node in self.nodes:
            print("node {0}: parent = {1}, sibling = {2}, degree = {3}, depth = {4}, height = {5}, {6}".
                  format(node.id,
                         node.parent,
                         node.sibling,
                         node.degree,
                         node.depth,
                         node.height,
                         node.type))

    def preorder_tree_walk(self, node_id, result):
        result.append(node_id)
        if self.nodes[node_id].left != -1:
            self.preorder_tree_walk(self.nodes[node_id].left, result)
        if self.nodes[node_id].right != -1:
            self.preorder_tree_walk(self.nodes[node_id].right, result)
        return result

    def inorder_tree_walk(self, node_id, result):
        if self.nodes[node_id].left != -1:
            self.inorder_tree_walk(self.nodes[node_id].left, result)
        result.append(node_id)
        if self.nodes[node_id].right != -1:
            self.inorder_tree_walk(self.nodes[node_id].right, result)
        return result

    def postorder_tree_walk(self, node_id, result):
        if self.nodes[node_id].left != -1:
            self.postorder_tree_walk(self.nodes[node_id].left, result)
        if self.nodes[node_id].right != -1:
            self.postorder_tree_walk(self.nodes[node_id].right, result)
        result.append(node_id)
        return result

if __name__ == '__main__':

    n = int(input())
    btree = BTree(n)

    for _ in range(n):
        al = [int(x) for x in input().split()]
        btree.add_children(*al)

    btree.update_type_depth()
    btree.update_height()

    root = btree.get_root()
    print("Preorder")
    result = btree.preorder_tree_walk(root, [])
    print(" " + " ".join([str(x) for x in result]))

    print("Inorder")
    result = btree.inorder_tree_walk(root, [])
    print(" " + " ".join([str(x) for x in result]))

    print("Postorder")
    result = btree.postorder_tree_walk(root, [])
    print(" " + " ".join([str(x) for x in result]))