import copy
import queue

hash_table = {}                             # 盤面（ハッシュ）を管理する辞書（テーブル）
directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
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
        self.r0, self.c0 = self.get0()          # ０の板の位置を記憶する

    def get0(self):
        """
        ０の板の位置を探索し返却する関数
        :return: r,c  ０の板の位置
        """
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == 0:
                    return r, c
        raise ValueError

    def make_hash(self, board):
        """
        盤面からハッシュ値を計算する
        単純に先頭から数字を連結したものをハッシュ値とする
        """
        h = 0
        for r in board:
            for c in r:
                h = h * 10 + c
        return h

    def get_next_board(self):
        """
        今の盤面から遷移可能な盤面を計算する。
        過去に遷移したことがある（ハッシュテーブルに登録されている）盤面は除外
        Boardクラスのリストとして返却する
        """
        board_class_list = []

        for dr, dc in directions:
            if 0 <= self.r0 + dr < 3 and 0 <= self.c0 + dc < 3:
                new_board = copy.deepcopy(self.board)
                t = new_board[self.r0 + dr][self.c0 + dc]
                new_board[self.r0 + dr][self.c0 + dc] = 0
                new_board[self.r0][self.c0] = t
                h = self.make_hash(new_board)
                if h not in hash_table:
                    b = Board(new_board, self.n + 1, self.h)
                    board_class_list.append(b)
                    hash_table[h] = b

        return board_class_list


def decode():
    board = []
    for _ in range(3):
        al = [int(x) for x in input().split()]
        board.append(al)
    return board

if __name__ == '__main__':

    q = queue.Queue()
    board = decode()
    board_c = Board(board, 0)
    q.put(board_c)

    flg = True
    while not q.empty() and flg:
        bc = q.get()
        bc_list = bc.get_next_board()
        for b in bc_list:
            if b.h == h_goal:
                print(b.n)
                flg = False
            else:
                q.put(b)

