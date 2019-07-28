BASE = 101
MASK = (1 << 64) - 1
BK = []

H = W = R = C = 0
tf = []
pf = []
pfh = []
tfh = []

def make_bk():
    global BK
    for k in range(C - 1, -1, -1):
        BK.append((BASE ** k) & MASK)


def make_pfh():
    global pfh
    for p in pf:
        h = 0
        for i, v in enumerate(p):
            h += ord(v) * BK[i]
            h = h & MASK
        pfh.append(h)


def make_tfh():
    global tfh

    tfh = [[-1] * W for _ in range(H)]
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
    make_bk()
    make_pfh()
    make_tfh()

    for i in range(H - R + 1):
        for j in range(W - C + 1):
            if tfh[i][j] == pfh[0]:
                flg = True
                for k in range(1, R):
                    if tfh[i + k][j] != pfh[k]:
                        flg = False
                        break
                if flg:
                    print(i, j)
