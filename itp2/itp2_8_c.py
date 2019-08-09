class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class Map:

    def __init__(self):
        self.root = Node("", 0)

    def insert(self, key, value):
        p = self.root
        newn = Node(key, value)
        while p.next:
            if p.next.key == key:
                p.next.value = value
                return
            if p.next.key > key:
                newn.next = p.next
                p.next = newn
                return
            else:
                p = p.next
        p.next = newn

    def get(self, key):
        p = self.root
        while p.next:
            if p.next.key == key:
                print(p.next.value)
                return
            else:
                p = p.next
        print(0)

    def delete(self, key):
        p = self.root

        while p.next:
            if p.next.key == key:
                p.next = p.next.next
                return
            elif p.next.key < key:
                p = p.next
            else:
                break

    def dump(self, l, r):
        p = self.root
        while p.next and p.next.key <= r:
            if p.next.key >= l:
                print(p.next.key, p.next.value)
            p = p.next

m = Map()
q = int(input())
for _ in range(q):
    query, *arg = input().split()
    query = int(query)
    if query == 0:
        m.insert(arg[0], int(arg[1]))
    elif query == 1:
        m.get(*arg)
    elif query == 2:
        m.delete(*arg)
    else:
        m.dump(*arg)