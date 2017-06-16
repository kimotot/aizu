class Tree:

    def __init__(self, n):
        self.nodes = [Node(i) for i in range(n)]

    def add_children(self, node_id, children):
        self.nodes[node_id].add_child(children)
        for child in children:
            self.nodes[child].update(node_id)

    def get_root(self):
        for node in self.nodes:
            if node.parent is None:
                root_id = node.id
                break
        return root_id

    def update_dt_child(self, node_id, depth):
        node = self.nodes[node_id]
        node.depth = depth
        if node.children:
            if node.type == "root":
                pass
            else:
                node.type = "internal node"
            for child in node.children:
                self.update_dt_child(child, depth + 1)
        else:
            if node.type == "root":
                pass
            else:
                node.type = "leaf"

    def update_dt(self):
        root_id = self.get_root()
        self.nodes[root_id].type = "root"
        self.nodes[root_id].parent = -1
        self.update_dt_child(root_id, 0)

    def disp(self):
        for node in self.nodes:
            print("node {0}: parent = {1}, depth = {2}, {3}, {4}".
                  format(node.id,
                         node.parent,
                         node.depth,
                         node.type,
                         node.children))

class Node:

    def __init__(self, n):
        self.id = n
        self.parent = None
        self.children = []
        self.type = None
        self.depth = None

    def add_child(self, children):
        self.children = children

    def update(self, parent_id):
        self.parent = parent_id

if __name__ == '__main__':

    n = int(input())
    tree = Tree(n)

    for _ in range(n):
        al = [int(x) for x in input().split()]
        id = al[0]
        children = al[2:]
        tree.add_children(id, children)

    tree.update_dt()

    tree.disp()