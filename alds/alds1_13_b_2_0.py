import copy
import collections

hash_table = {}                             # 盤面（ハッシュ）を管理する辞書（テーブル）
directions = ((1, 3),
              (0, 2, 4),
              (1, 5),
              (0, 4, 6),
              (1, 3, 5, 7),
              (2, 4, 8),
              (3, 7),
              (4, 6, 8),
              (5, 7))

h_goal = 123456780

class Board:
    """
    ８パズルの盤面の情報を保持するクラス
    """

    def __init__(self, board, n, prev=None):
        self.board = board                      # 盤面の情報　3×3配列
        self.h = self.make_hash(self.board)     # 盤面をハッシュ値に変換したもの
        self.prev = prev                        # この１手前の盤面を指すハッシュ値
        self.n = n                              # この盤面に到達するまでの手数
        self.space = board.index(0)             # ０の板の位置を記憶する

    def make_hash(self, board):
        """
        盤面からハッシュ値を計算する
        単純に先頭から数字を連結したものをハッシュ値とする
        """
        h = 0
        for i in board:
            h = h * 10 + i
        return h

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
            h = self.make_hash(new_board)
            if h not in hash_table:
                b = Board(new_board, self.n + 1, self.h)
                board_class_list.append(b)
                hash_table[h] = True

        return board_class_list


def decode():
    board = []
    for _ in range(3):
        al = [int(x) for x in input().split()]
        board.extend(al)
    return board

if __name__ == '__main__':

    q = collections.deque()
    board = decode()
    board_c = Board(board, 0)
    hash_table[board_c.h] = True
    q.append(board_c)

    while len(q) != 0:
        bc = q.popleft()

        if bc.h == h_goal:
            print(bc.n)
            break

        bc_list = bc.get_next_board()
        for b in bc_list:
            q.append(b)

