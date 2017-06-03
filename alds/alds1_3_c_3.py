class dllist:

<<<<<<< HEAD
    def __init__(self):
        self._list = []
        self._fp = 0
        self._bp = 0

    def insert(self, x):
        self._list.append(x)
        self._fp += 1

    def delete(self, x):
        t = self._list[::-1]
        if x in t[:-self._bp]:
            self._list.remove(x)
            self._fp -= 1

    def deleteFirst(self):
        self._list.pop()

    def deleteLast(self):
        self._bp += 1

    def disp(self):
        print(" ".join([str(x) for x in self._list[self._bp:][::-1]]))


if __name__ == '__main__':

    q = dllist()

    n = int(input())

    for _ in range(n):
        inst = input().split()

        if inst[0] == "insert":
            q.insert(int(inst[1]))
        elif inst[0] == "delete":
            q.delete(int(inst[1]))
        elif inst[0] == "deleteFirst":
            q.deleteFirst()
        elif inst[0] == "deleteLast":
            q.deleteLast()

    q.disp()

=======
    class node:
        def __init__(self, key, parent, child):
            self._key = key
            self._parent = parent
            self._child = child

        def getkey(self):
            return self._key

        def getparent(self):
            return self._parent

        def setparent(self, node):
            self._parent = node

        def getchild(self):
            return self._child

        def setchild(self, node):
            self._child = node

    def __init__(self):
        self._child = None

    def setchild(self, node):
        self._child = node

    def insert(self, key):
        anode = self.node(key, self, self._child)
        self._child = anode
        if anode.getchild() is not None:
            anode.getchild().setparent(anode)

    def delete(self, key):
        idx = self._child
        while idx is not None:
            if idx.getkey() == key:
                idx.getparent().setchild(idx.getchild())
                if idx.getchild() is not None:
                    idx.getchild().setparent(idx.getparent())
                del idx
                return
            else:
                idx = idx.getchild()

    def deleteFirst(self):
        if self._child is not None:
            t = self._child
            self._child = t.getchild()
            self._child.setparent(self)
            del t

    def deleteLast(self):
        if self._child is not None:
            idx = self._child
            while idx.getchild() is not None:
                idx = idx.getchild()
            idx.getparent().setchild(None)
            del idx

if __name__ == '__main__':

    root = dllist()

    n = int(input())
    for _ in range(n):
        al = input().split()
        if al[0] == "insert":
            root.insert(int(al[1]))
        elif al[0] == "delete":
            root.delete(int(al[1]))
        elif al[0] == "deleteFirst":
            root.deleteFirst()
        elif al[0] == "deleteLast":
            root.deleteLast()

    ans = []
    idx = root._child
    while idx is not None:
        ans.append(idx.getkey())
        idx = idx.getchild()

    print(" ".join([str(x) for x in ans]))
>>>>>>> origin/master
