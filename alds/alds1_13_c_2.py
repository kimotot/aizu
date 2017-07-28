import copy
import collections
import heapq
import itertools

FORWARD = 1
BACKWARD = -1
REMOVED = ''

hash_table = {}                             # 盤面（ハッシュ）を管理する辞書（テーブル）
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

goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

class PrioriyQueue:
    """
    優先度付キュー
    """
    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        counter = itertools.count()

    def add_boardclass(self, boardclass):
        if boardclass.h in self.entry_finder:
            self.remove_boardclass(boardclass)
        count 

class Board:
    """
    １５パズルの盤面の情報を保持するクラス
    """

    def __init__(self, board, n, d):
        self.board = board                      # 盤面の情報　3×3配列
        self.h = tuple(self.board)              # 盤面をハッシュ値に変換したもの
        self.n = n                              # この盤面に到達するまでの手数
        self.space = board.index(0)             # ０の板の位置を記憶する
        self.dic = d                            # 検索方向


def decode():
    board = []
    for _ in range(4):
        al = [int(x) for x in input().split()]
        board.extend(al)
    return board

if __name__ == '__main__':

    q = collections.deque()
    board = decode()

    if board == goal:
        print(0)
    else:
        board_s = Board(board, 0, FORWARD)
        hash_table[board_s.h] = board_s
        q.append(board_s)

        board_e = Board([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0], 0, BACKWARD)
        hash_table[board_e.h] = board_e
        q.append(board_e)

        flg = True
        while q and flg:
            bc = q.popleft()

            for d in directions[bc.space]:
                new_board = copy.copy(bc.board)
                t = new_board[d]
                new_board[d] = 0
                new_board[bc.space] = t
                h = tuple(new_board)

                if h in hash_table and hash_table[h].dic != bc.dic:
                    print(bc.n + hash_table[h].n + 1)
                    flg = False
                    break
                elif h not in hash_table:
                    b = Board(new_board, bc.n + 1, bc.dic)
                    hash_table[h] = b
                    q.append(b)



