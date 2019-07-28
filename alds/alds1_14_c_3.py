BASE = 101
BASE2 = 103
MASK = (1 << 64) - 1
BK = []
BK2 = []

H = W = R = C = 0
tf = []
pf = []


def make_bk():
    global BK, BK2
    for k in range(C - 1, -1, -1):
        BK.append((BASE ** k) & MASK)

    for k in range(R - 1, -1, -1):
        BK2.append((BASE2 ** k) & MASK)


def make_pfh():
    pfh = []
    for p in pf:
        h = 0
        for i, v in enumerate(p):
            h += ord(v) * BK[i]
            h = h & MASK
        pfh.append(h)

    res = 0
    for i, v in enumerate(pfh):
        res += v * BK2[i]
        res &= MASK

    return res


def make_tfh():
    tfh = [[-1] * W for _ in range(H)]
    t_hash = [[None] * (W - C + 1) for _ in range(H - R + 1)]

    for i in range(H):
        h = 0
        for k in range(C):
            h += ord(tf[i][k]) * BK[k]
            h &= MASK
        tfh[i][0] = h

        for j in range(1, W - C + 1):
            h = h - (ord(tf[i][j - 1]) * BK[0])
            h *= BASE
            h += ord(tf[i][j + C - 1])
            h &= MASK
            tfh[i][j] = h

    for j in range(W - C + 1):
        tmp = 0
        for i in range(R):
            tmp += tfh[i][j] * BK2[i]
            tmp &= MASK
        t_hash[0][j] = tmp

    for j in range(W - C + 1):
        for i in range(1, H - R + 1):
            tmp = t_hash[i - 1][j]
            tmp -= tfh[i - 1][j] * BK2[0]
            tmp *= BASE2
            tmp += tfh[i + R - 1][j]
            tmp &= MASK
            t_hash[i][j] = tmp

    return t_hash


def decode():
    global H, W, R, C, tf, pf
    H, W = [int(x) for x in input().split()]
    for _ in range(H):
        tf.append(input())

    R, C = [int(x) for x in input().split()]
    for _ in range(R):
        pf.append(input())


if __name__ == "__main__":
    decode()

    if W >= C and H >= R:
        make_bk()
        p_hash = make_pfh()
        t_hash = make_tfh()

        for i in range(H - R + 1):
            for j in range(W - C + 1):
                if t_hash[i][j] == p_hash:
                    print(i, j)
