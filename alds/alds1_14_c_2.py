BASE = ord('0')

def decode():
    # 入力を受け取りグローバル変数にセットする
    # H : 検索対象となる文字フィールドの縦行数
    # W : 検索対象となる文字フィールドの横列数
    # R : 文字パターンの縦行数
    # C : 文字パターンの横列数
    # sf : 文字フィールド　リストを使った二次元配列
    # pt : 文字パターン
    global H, W, R, C, sf, pt

    [H, W] = [int(x) for x in input().split()]
    sf = []
    for _ in range(H):
        sf.append(input())

    [R, C] = [int(x) for x in input().split()]
    pt = []
    for _ in range(R):
        pt.append(input())


def tord(c):
    # 文字"0"を基底=0とした文字コードを変換したものを返す
    return ord(c) - BASE


def mk_table(pt, m):
    # ptに従い、事前に文字毎の移動量を計算し、グローバル変数mtにセットする
    global mt
    mt = [m] * (tord("z") + 1)
    m = m - 1
    for i in range(m):
        mt[tord(pt[i])] = m - i


def line_search(s, p, n):
    # 文字列Sのn番目(0相対）から検索を始めて、文字列pと等しい先頭位置を求める
    # 見つからなかった場合は-1を返す
    global mt
    lens = len(s)
    lenp = len(p)
    wlimit = lens - lenp + 1
    # n = 0
    while n < wlimit:
        j = lenp - 1
        while j >= 0:
            if s[n + j] != p[j]:
                break
            j -= 1
        if j < 0:
            return n
        else:
            n += mt[tord(s[n + lenp - 1])]
    return -1


def isfind(i, j):
    # i行、j列（左上）から始めて、ptと一致するかチェックする
    flg = True
    for k in range(1, R):
        if sf[i + k][j:j + C] != pt[k]:
            flg = False
            break
    return flg


if __name__ == "__main__":
    H = W = R = C = 0
    sf = []
    pt = []
    mt = []

    decode()
    mk_table(pt[0], C)

    for i in range(H - R + 1):
        j = 0
        while True:
            j = line_search(sf[i], pt[0], j)
            if j == -1:
                break
            else:
                if isfind(i, j):
                    print(i, j)
                j += 1
