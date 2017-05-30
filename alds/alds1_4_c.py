class dictionary:

    def __init__(self):
        self._d = set()

    def insert(self, s):
        self._d.add(s)

    def find(self, s):
        if s in self._d:
            print("yes")
        else:
            print("no")


if __name__ == '__main__':

    dd = dictionary()

    n = int(input())
    for _ in range(n):
        args = input().split()
        if args[0] == "insert":
            dd.insert(args[1])
        elif args[0] == "find":
            dd.find(args[1])
