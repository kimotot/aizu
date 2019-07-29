END = float('inf')


class Node:

    def __init__(self, n, prev=None, next=None):
        self.n = n
        self.prev = prev
        self.next = next


class List:

    def __init__(self):
        self.index = Node(END)

    def insert(self, x):
        new_node = Node(x)
        new_node.prev = self.index.prev
        new_node.next = self.index
        if self.index.prev is not None:
            self.index.prev.next = new_node
        self.index.prev = new_node
        self.index = new_node

    def move(self, d):
        if d > 0:
            for _ in range(d):
                self.index = self.index.next
        else:
            for _ in range(-d):
                self.index = self.index.prev

    def erase(self):
        if self.index.prev is not None:
            self.index.prev.next = self.index.next

        self.index.next.prev = self.index.prev
        self.index = self.index.next

    def dump(self):
        idx = self.index
        while idx.prev is not None:
            idx = idx.prev

        while idx.n != END:
            print(idx.n)
            idx = idx.next


if __name__ == "__main__":
    q = int(input())

    li = List()
    for _ in range(q):
        query = input()
        order = int(query[0])
        if order != 2:
            parm = int(query[2:])

        if order == 0:
            li.insert(parm)
        elif order == 1:
            li.move(parm)
        else:
            li.erase()

    li.dump()


