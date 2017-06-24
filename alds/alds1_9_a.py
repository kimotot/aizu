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


if __name__ == '__main__':

    h = int(input())
    hlist = [int(x) for x in input().split()]

    cbt = Heap(h, hlist)
    cbt.disp()


