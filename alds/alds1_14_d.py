BASE = 101
MASK = (1 << 64) - 1


def calc_hash(t, tl, pl):
    res = set()

    tmp = 0
    for i in range(pl):
        tmp *= BASE
        tmp += t[i]
        tmp &= MASK
    res.add(tmp)

    BASE_K = 1
    for _ in range(pl):
        BASE_K = (BASE_K * BASE) & MASK

    for i in range(1, tl - pl + 1):
        tmp -= t[i - 1] * BASE_K
        tmp *= BASE
        tmp += t[i + pl - 1]
        tmp &= MASK
        res.add(tmp)

    return res


if __name__ == "__main__":

    t = tuple(ord(c) for c in input())
    tl = len(t)

    q = int(input())
    ps = []
    for _ in range(q):
        ps.append(tuple(ord(c) for c in input()))

    hd = {}            # 文字列Tから、長さnの部分文字列を作った際のハッシュ値を保持する辞書

    for p in ps:
        pl = len(p)

        if pl > tl:
            print("0")
        else:
            bs = min(19, pl)
            ph = calc_hash(p, pl, bs)

            if pl in hd:
                th = hd[pl]
            else:
                th = calc_hash(t, tl, bs)
                hd[pl] = th

            if ph.issubset(th):
                print("1")
            else:
                print("0")
