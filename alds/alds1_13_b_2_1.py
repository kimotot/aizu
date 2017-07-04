# coding: utf-8
#
# eight.py : 8 Puzzle (幅優先探索による解法)
#
#            Copyright (C) 2007 Makoto Hiroi
#
from collections import deque
import time

# 隣接リスト
adjacent = (
    (1, 3),       # 0
    (0, 2, 4),    # 1
    (1, 5),       # 2
    (0, 4, 6),    # 3
    (1, 3, 5, 7), # 4
    (2, 4, 8),    # 5
    (3, 7),       # 6
    (4, 6, 8),    # 7
    (5, 7)        # 8
)

# ゴールの局面
GOAL = [1, 2, 3, 4, 5, 6, 7, 8, 0]

##### 幅優先探索 #####

# 局面の定義
class State:
    def __init__(self, board, space, prev):
        self.board = board
        self.space = space
        self.prev = prev


def bf_search(start):
    q = deque()
    q.append(State(start, start.index(0), None))
    table = {}
    table[tuple(start)] = True
    while len(q) > 0:
        a = q.popleft()
        for x in adjacent[a.space]:
            b = a.board[:]
            b[a.space] = b[x]
            b[x] = 0
            key = tuple(b)
            if key in table: continue
            c = State(b, x, a)
            if b == GOAL:
                print_answer(c)
                return
            q.append(c)
            table[key] = True

# 表示
def print_answer(x):
    if x is not None:
        print_answer(x.prev)
        print(x.board)


if __name__ == '__main__':

    bf_search([2,5,6,7,4,0,3,8,1])
