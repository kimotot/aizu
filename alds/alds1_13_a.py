import functools

QUEEN = 1
EMPTY = 0
directions = {(r, c) for r in range(-1, 2) for c in range(-1, 2) if not(r == 0 and c == 0)}

def decode():
    board = [[EMPTY] * 8 for _ in range(8)]

    n = int(input())
    for _ in range(n):
        [r, c] = [int(x) for x in input().split()]
        board[r][c] = QUEEN

    return board


def disp_board(board):
    for r in board:
        str = ""
        for c in r:
            if c == QUEEN:
                str += "Q"
            else:
                str += "."
        print(str)


def isput(board, r, c):
    for (rd, cd) in directions:
        rn = r + rd
        cn = c + cd
        while 0 <= rn < 8 and 0 <= cn < 8:
            if board[rn][cn] == QUEEN:
                return False
            rn += rd
            cn += cd

    return True


def put(board, r):
    if r >= 8:
        disp_board(board)
    else:
        if functools.reduce(lambda x, y: x or y, board[r]):
            put(board, r+1)
        else:
            for c in range(8):
                if isput(board, r, c):
                    board[r][c] = True
                    put(board, r+1)
                    board[r][c] = False


if __name__ == '__main__':

    board = decode()
    put(board, 0)