class PQ:

    def __init__(self, h_max = 2000000):
        self.h_max = h_max
        self.h = 0
        self.heap = [None for _ in range(h_max + 1)]

    def swap(self, a, b):
        t = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = t

    def larger_up(self, n):
        if n > 1:
            parent_n = n // 2
            if self.heap[n] > self.heap[parent_n]:
                self.swap(n, parent_n)
                self.larger_up(parent_n)

    def smaller_down(self, n):
        left_n = n * 2
        right_n = n * 2 + 1

        if left_n <= self.h and self.heap[left_n] > self.heap[n]:
            max_n = left_n
        else:
            max_n = n

        if right_n <= self.h and self.heap[right_n] > self.heap[max_n]:
            max_n = right_n

        if max_n != n:
            self.swap(max_n, n)
            self.smaller_down(max_n)

    def insert(self, k):
        self.h += 1
        self.heap[self.h] = k
        self.larger_up(self.h)

    def extractmax(self):
        t = self.heap[1]
        self.heap[1] = self.heap[self.h]
        self.h -= 1
        self.smaller_down(1)
        return t

if __name__ == '__main__':

    pq = PQ()

    while True:
        inst = input()
        if inst[0] == 'i':
            pq.insert(int(inst[7:]))
        elif inst[1] == "x":
            print(pq.extractmax())
        else:
            break



