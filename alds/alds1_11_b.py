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


def dfs(s_id):
    global nodes, ts
    nodes[s_id].d = ts
    ts += 1

    for next_id in nodes[s_id].next_list:
        if nodes[next_id].d is None:
            dfs(next_id)

    nodes[s_id].f = ts
    ts += 1


if __name__ == '__main__':

    n = int(input())
    nodes = [None] * (n + 1)
    for _ in range(n):
        id, _, *next_list = [int(x) for x in input().split()]
        nodes[id] = Node(id, next_list)

    ts = 1
    for i in range(1, n+1):
        if nodes[i].d is None:
            dfs(i)

    for i in range(1, n+1):
        nodes[i].disp()


