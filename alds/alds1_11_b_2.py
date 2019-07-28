# スタックを用いて深さ優先探索を行う


class Node:
    '''
    グラフのノードを表現するクラス
    '''

    def __init__(self, node_id, next_list):
        self.node_id = node_id          # ノードID
        self.next_list = next_list      # 隣接ノードのリスト
        self.nc = 0                     # 隣接ノードリストで次に検索すべきノードの番号 先頭が0 存在しない場合はNone
        self.d = None                   # 発見(discoverd)したタイムスタンプ
        self.f = None                   # そのノード経由のルート探索が全て完了した時刻を示すタイムスタンプ

        if next_list:
            self.nc = 0

    def next_node(self):
        '''
        隣接ノードリストの中から、次に探索すべきノードを見つけてかえす
        候補ノードがすでに発見済の場合はパスする
        ノードがない（リストが空もしくは最後まで探索した）場合はNoneを返す
        '''

        global nodes

        while self.nc < len(self.next_list):            # 隣接ノードリストの末尾まで繰り返す
            next_id = self.next_list[self.nc]           # 次に探索すべき候補ノードのidを求める
            self.nc += 1                                # 隣接ノードリストの参照カウンタを一つ進める
            if nodes[next_id].d is None:                # 候補ノードが未発見の場合
                return next_id                          # そのノードIDを返す

        return None                                     # 候補ノードが見つからない場合はNoneを返す


    def disp(self):
        '''
        ノードの情報を表示する
        自ノードID, 発見時タイムスタンプ, 探索完了タイムスタンプ
        '''
        print("{0} {1} {2}".format(self.node_id, self.d, self.f))

    def debug_disp(self):
        self.disp()
        print(self.next_list)


def dfs():
    global nodes, ts, stack

    while stack:                                # スタックに要素がある限り続ける
        node_id = stack[-1]                     # スタックの最上位（末尾）の要素を参照する
        next_id = nodes[node_id].next_node()    # 次に探索すべき隣接ノードを求める

        if next_id is None:                     # 次に探索すべき隣接ノードがない（全て探索した）場合
            stack.pop()                         # スタックから最上位の要素を取り出す
            nodes[node_id].f = ts               # そのノードに関する探索が完了したので完了タイムスタンプを記録
            ts += 1                             # 次の記録に備えてタイムスタンプを進める
        else:
            nodes[next_id].d = ts               # 探索候補ノードの発見時刻を記録する
            ts += 1
            stack.append(next_id)               # 探索候補ノードをスタックに積む


if __name__ == '__main__':

    n = int(input())

    # ノード情報を保持するリストを用意する
    nodes = [None] * (n + 1)            # ノード番号が１相対なので、nodes[0]は使わない

    # 探索用のスタックを用意する
    stack = []

    # 隣接ノードの情報を保存する
    for _ in range(n):
        id, _, *next_list = [int(x) for x in input().split()]
        nodes[id] = Node(id, next_list)

    # タイムスタンプを初期化
    ts = 1

    # 未発見ノードがあれば、それを始点として深さ優先探索を行う
    # 連結グラフであれば、この処理は意味がない⇒一度の探索で必ず全てのノードを発見する
    for i in range(1, n+1):
        if nodes[i].d is None:
            nodes[i].d = ts
            ts += 1
            stack.append(i)
            dfs()

    for i in range(1, n+1):
        nodes[i].disp()


