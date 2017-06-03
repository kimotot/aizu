class dllist:

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

