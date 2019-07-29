import heapq as hq
ALP = "abcdefghijklmnopqrstuvwxyz"

class Node:

    def __init__(self, priority, value=None, parent=None):
        self.priority = priority
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def __eq__(self, other):
        return self.priority == other.priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __ge__(self, other):
        return self.priority >= other.priority

    def __ne__(self, other):
        return self.priority != other.priority


class Huffman:

    def __init__(self):
        self.s = None
        self.q = []
        self.root = None
        self.p = dict()
        self.hc = dict()

    def addinitnode(self, s):
        self.s = s
        for a in s:
            self.p[a] = self.p.get(a, 0) + 1
        for a, pri in self.p.items():
            hq.heappush(self.q, Node(value=a, priority=pri))

    def makebtree(self):
        while self.q:
            if len(self.q) == 1:
                self.root = hq.heappop(self.q)
                self.root.parent = self.root
            else:
                na = hq.heappop(self.q)
                nb = hq.heappop(self.q)

                nn = Node(na.priority + nb.priority)
                nn.left = na
                nn.right = nb
                na.parent = nn
                nb.parent = nn

                hq.heappush(self.q, nn)

    def gethuffmancode(self):

        def ghc(r, depth):
            if r.value is not None:
                self.hc[r.value] = depth
            else:
                ghc(r.left, depth + 1)
                ghc(r.right, depth + 1)

        if self.root.value is not None:
            self.hc[self.root.value] = 1
        else:
            ghc(self.root, 0)

    def gethuffmanlen(self):

        ans = 0
        for a in self.s:
            ans += self.hc[a]

        return ans

if __name__ == "__main__":
    S = input()

    hf = Huffman()
    hf.addinitnode(S)
    hf.makebtree()
    hf.gethuffmancode()
    print(hf.gethuffmanlen())