class PriorityQueue:

    def __init__(self):

        self.q = []


    def insert(self, k):
        self.q.append(k)

    def extractMax(self):
        result = max(self.q)
        self.q.remove(result)
        return result


if __name__ == '__main__':

    q = PriorityQueue()
    while True:
        al = input().split()

        if al[0] == "insert":
            q.insert(int(al[1]))
        elif al[0] == "extract":
            print(q.extractMax())
        elif al[0] == "end":
            break

        max
