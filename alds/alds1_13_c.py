import copy
import collections

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

h_goal = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)

class Board:
    """
    １５パズルの盤面の情報を保持するクラス
    """

    def __init__(self, board, n, prev=None):
        self.board = board                      # 盤面の情報　3×3配列
        self.h = tuple(self.board)              # 盤面をハッシュ値に変換したもの
        self.prev = prev                        # この１手前の盤面を指すハッシュ値
        self.n = n                              # この盤面に到達するまでの手数
        self.space = board.index(0)             # ０の板の位置を記憶する

    def get_next_board(self):
        """
        今の盤面から遷移可能な盤面を計算する。
        過去に遷移したことがある（ハッシュテーブルに登録されている）盤面は除外
        Boardクラスのリストとして返却する
        """
        board_class_list = []

        for d in directions[self.space]:
            new_board = copy.copy(self.board)
            t = new_board[d]
            new_board[d] = 0
            new_board[self.space] = t
            h = tuple(new_board)
            if h not in hash_table:
                b = Board(new_board, self.n + 1, self.h)
                board_class_list.append(b)
                hash_table[h] = True

        return board_class_list


def decode():
    board = []
    for _ in range(4):
        al = [int(x) for x in input().split()]
        board.extend(al)
    return board

if __name__ == '__main__':

    q = collections.deque()
    board = decode()
    board_c = Board(board, 0)
    hash_table[board_c.h] = True
    q.append(board_c)

    while q:
        bc = q.popleft()

        if bc.h == h_goal:
            print(bc.n)
            break
        else:
            bc_list = bc.get_next_board()
            q.extend(bc_list)


