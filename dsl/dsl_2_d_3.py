# Range Update Query(RUQ)
INF = 2 ** 31 - 1


class RUQ:

    class NODE:

        def __init__(self):
            # ノードの初期値は無限大(INF)
            #
            self.data = INF
            self.lazy = None

    def __init__(self, n):
        # n個のデータを保持するセグメント木の葉の個数を求める
        # 2のx乗で,xを順に増加してゆき、nを超えるまで繰り返す
        self.n0 = 1
        while self.n0 < n:
            self.n0 *= 2         # 葉の最初の要素のindexは0相対で n0-1 となる

        # セグメント木の入れ物（配列）を用意する
        # 配列の要素数は (2*n0 - 1) 個
        # 要素の内容は　data:無限大(INF) lazy:なし(None)
        self.seg = [RUQ.NODE() for _ in range(2 * self.n0 - 1)]

    def lazy_update(self, k):
        # k番目の要素に対して遅延評価を行う
        if self.seg[k].lazy is not None:
            # lazyが存在すれば、lazyのデータで本データを更新
            self.seg[k].data += self.seg[k].lazy

            # 自分が葉でなければ、子ノードのlazyに親ノードのlazyを伝播
            if k < self.n0:
                self.seg[2*k+1].lazy = self.seg[k].lazy
                self.seg[2*k+2].lazy = self.seg[k].lazy

            # 伝播が終わったので、lazyを初期化　Noneに戻す
            self.seg[k].lazy = None

    def _update(self, s, t, x, k, l, r):
        # 区間[s, t) をxに更新する
        # k番目のセグ木要素に着目し、そこから更新を始める
        # k番目の要素の担当範囲が[l,r) 半開放区間

        # 遅延評価
        self.lazy_update(k)

        # 区間がまったくかぶらない
        if t <= l and r <= s:
            return
        # 完全にかぶるとき
        elif s <= l and r <= t:
            self.seg[k].lazy = x
            self.lazy_update(self, k)
            return
        # 区間がかさなるけどはみでるとき
        else:
            self._update(self, s, t, x, 2*k+1, l, (r-l)//2+l)
            self._update(self, s, t, x, 2*k+2, (r-l)//2+l, r)
            return

    def update(self, s, t, x):
        self._update(self, s, t+1, x, 0, 0, self.n0)

    def _find(self, s, t, k, l, r):
        # 遅延評価
        self.lazy_update(k)

        if r - l == 1:
            return self.seg[l].data

        # 区間がまったくかぶらない
        if t <= l and r <= s:
            return None

        # 区間がかさなるけどはみでるとき
        dl = self._find(self, s, t, 2*k+1, l, (r-l)//2+l)
        dr = self._find(self, s, t, 2*k+2, (r-l)//2+l, r)

        if dl is None and dr is None:
            return None
        elif dl is not None and dr is None:
            return dl
        elif dl is None and dr is not None:
            return dr
        else:
            return -1

    def find(self, s):
        return self._find(self, s, s + 1, 0, 0, self.n0)


if __name__ == "__main__":
    n, q = map(int, input().split())
    ruq = RUQ(n)

    for _ in range(q):
        query, *arg = map(int, input().split())
        if query == 0:
            ruq.update(*arg)
        else:
            print(ruq.find(*arg))