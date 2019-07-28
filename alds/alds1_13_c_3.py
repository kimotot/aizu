import copy
import heapq

directions = ((1, 4),           #0
              (0, 2, 5),        #1
              (1, 3, 6),        #2
              (2, 7),           #3
              (0, 5, 8),        #4
              (1, 4, 6, 9),     #5
              (2, 5, 7, 10),    #6
              (3, 6, 11),       #7
              (4, 9, 12),       #8
              (5, 8, 10, 13),   #9
              (6, 9, 11, 14),   #10
              (7, 10, 15),      #11
              (8, 13),          #12
              (9, 12, 14),      #13
              (10, 13, 15),     #14
              (11, 14))         #15

bantoxy = ((0, 0), (1, 0), (2, 0), (3, 0),
           (0, 1), (1, 1), (2, 1), (3, 1),
           (0, 2), (1, 2), (2, 2), (3, 2),
           (0, 3), (1, 3), (2, 3), (3, 3))

goalxy = ((3, 3),
          (0, 0), (1, 0), (2, 0), (3, 0),
          (0, 1), (1, 1), (2, 1), (3, 1),
          (0, 2), (1, 2), (2, 2), (3, 2),
          (0, 3), (1, 3), (2, 3))


goalh = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)


class Board:
    """
    １５パズルの盤面の情報を保持するクラス
    """

    def __init__(self, ban, n):
        self.ban = ban                          # 盤面の情報　0～16の一元配列
        self.h = tuple(self.ban)                # 盤面をハッシュ値に変換したもの　単純にタプルに変換したもの
        self.n = n                              # この盤面に到達するまでの手数
        self.space = ban.index(0)               # ０の板の位置を記憶する
        self.cost = self.calc_cost(ban)         # ゴールまでに係るコスト（マンハッタン数で代用）

    def calc_cost(self, ban):
        tmp = 0
        for i, v in enumerate(self.ban):
            if v == 0:
                pass
            else:
                x1, y1 = bantoxy[i]
                x2, y2 = goalxy[v]
                tmp += abs(x1 - x2)
                tmp += abs(y1 - y2)
        return tmp * 1.2 + self.n

    def __eq__(self, other):
        return self.cost == other.cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __le__(self, other):
        return self.cost <= other.cost

    def __gt__(self, other):
        return self.cost > other.cost

    def __ge__(self, other):
        return self.cost >= other.cost

    def __ne__(self, other):
        return self.cost != other.cost


def decode():
    ban = []
    for _ in range(4):
        al = [int(x) for x in input().split()]
        ban.extend(al)
    return ban


if __name__ == '__main__':

    ban = decode()
    q = []
    hash_table = {}  # 盤面（ハッシュ）を管理する辞書（テーブル）

    board = Board(ban, 0)
    hash_table[board.h] = True
    heapq.heappush(q, board)

    while q:
        board = heapq.heappop(q)

        if board.h == goalh:
            print(board.n)
            break

        for d in directions[board.space]:
            new_ban = copy.copy(board.ban)
            t = new_ban[d]
            new_ban[d] = 0
            new_ban[board.space] = t
            h = tuple(new_ban)

            if h not in hash_table:
                heapq.heappush(q, Board(new_ban, board.n + 1))
                hash_table[h] = True

