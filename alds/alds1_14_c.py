def isin(sx, sy):
    for j in range(r):
        for i in range(c):
            if t[sy + j][sx + i] != p[j][i]:
                return False
    return True

[h, w] = [int(x) for x in input().split()]

t = []
for _ in range(h):
    t.append(input())

[r, c] = [int(x) for x in input().split()]
p = []
for _ in range(r):
    p.append(input())

for sy in range(h - r + 1):
    for sx in range(w - c + 1):
        if isin(sx, sy):
            print("{0} {1}".format(sy, sx))



