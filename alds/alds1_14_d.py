BASE = 127
MASK = (1 << 32) - 1
BASE_D = {}

def calc_hash(t, tl, pl):
    res = set()

    tmp = 0
    for i in range(pl):
        tmp = (tmp * BASE + t[i]) & MASK
    res.add(tmp)

    if pl - 1 in BASE_D:
        BASE_K = BASE_D[pl - 1]
    else:
        BASE_K = 1
        for _ in range(pl - 1):
            BASE_K = (BASE_K * BASE) & MASK
        BASE_D[pl - 1] = BASE_K

    for i in range(1, tl - pl + 1):
        tmp = ((tmp - t[i - 1] * BASE_K) * BASE + t[i + pl - 1]) & MASK
        res.add(tmp)

    return res


if __name__ == "__main__":

    t = tuple(ord(c) for c in input())
    tl = len(t)

    q = int(input())

    hd = {}
    ans = []

    for _ in range(q):
        p = tuple(ord(c) for c in input())
        pl = len(p)

        if pl > tl:
            ans.append("0")
        else:
            bs = min(19, pl)
            ph = calc_hash(p, pl, bs)

            if bs in hd:
                th = hd[bs]
            else:
                th = calc_hash(t, tl, bs)
                hd[bs] = th

            if ph.issubset(th):
                ans.append("1")
            else:
                ans.append("0")

    print("\n".join(ans))