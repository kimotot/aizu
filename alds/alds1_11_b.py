class Node:

    def __init__(self, node_id, next_list):
        self.node_id = node_id
        self.next_list = next_list
        self.d = None
        self.f = None

    def disp(self):
        print("{0} {1} {2}".format(self.node_id, self.d, self.f))

    def debug_disp(self):
        self.disp()
        print(self.next_list)


def dfs(s_id, ts):
    global nodes
    nodes[s_id].d = ts

    for next_id in nodes[s_id].next_list:
        if nodes[next_id].d is None:
            ts = dfs(next_id, ts + 1)
    ts += 1
    nodes[s_id].f = ts
    return ts

if __name__ == '__main__':

    n = int(input())
    nodes = {}
    for _ in range(n):
        al = [int(x) for x in input().split()]
        nodes[al[0]] = Node(al[0], al[2:])

    ts = 0
    for i in range(1, n+1):
        if nodes[i].d is None:
            ts = dfs(i, ts + 1)

    for i in range(1, n+1):
        nodes[i].disp()


