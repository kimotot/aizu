import random
import alds.mypkg as BT


tree = BT.BinaryTree.BinaryTree()
for _ in range(20):
    tree.insert(random.randint(0, 1000))
tree.show_list()
tree.delete(999)
tree.show_list()

