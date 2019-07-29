base = 101
mask = (1 << 32) - 1


def calc_hash(f, pl, tl):
    dl = tl - pl
    tmp = set()
    t = 1
    for _ in range(pl):
        t = (t * base) & mask
    e = 0
    for i in range(pl):
        e = (e * base + f[i]) & mask
    for i in range(dl):
        tmp.add(e)
        e = (e * base - t * f[i] + f[i + pl]) & mask
    tmp.add(e)
    return tmp


t = tuple(ord(c) for c in input())
tl = len(t)
q = int(input())
h = dict()
a = []

for _ in range(q):
    p = tuple(ord(c) for c in input())
    pl = len(p)
    if pl > tl:
        a.append("0")
        continue
    bs = min(19, pl)
    keys = calc_hash(p, bs, pl)
    if bs not in h:
        h[bs] = calc_hash(t, bs, tl)
    a.append("1" if keys <= h[bs] else "0")
print('\n'.join(a))