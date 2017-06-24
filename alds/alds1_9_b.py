class Heap:

    def __init__(self, h, hlist):

        self.heap = [None] + hlist
        self.h = h

    def disp(self):
        for node_id in range(1, self.h + 1):
            ans = "node {0}: key = {1}, ".format(node_id, self.heap[node_id])

            parent_id = node_id // 2
            if parent_id > 0:
                ans += "parent key = {0}, ".format(self.heap[parent_id])

            left_id = node_id * 2
            if left_id <= self.h:
                ans += "left key = {0}, ".format(self.heap[left_id])

            right_id = node_id * 2 + 1
            if right_id <= self.h:
                ans += "right key = {0}, ".format(self.heap[right_id])

            print(ans)

    def maxHeapify(self, root_id):
        left_id = root_id * 2
        right_id = root_id * 2 + 1

        if left_id <= self.h and self.heap[left_id] > self.heap[root_id]:
            largest = left_id
        else:
            largest = root_id

        if right_id <= self.h and self.heap[right_id] > self.heap[largest]:
            largest = right_id

        if largest != root_id:
            t = self.heap[root_id]
            self.heap[root_id] = self.heap[largest]
            self.heap[largest] = t
            self.maxHeapify(largest)

    def buildMaxHeap(self):
        for i in range(self.h // 2, 0, -1):
            self.maxHeapify(i)

if __name__ == '__main__':

    h = int(input())
    hlist = [int(x) for x in input().split()]

    maxheap = Heap(h, hlist)
    maxheap.buildMaxHeap()

    print("".join([" " + str(x) for x in maxheap.heap[1:]]))

