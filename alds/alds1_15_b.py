N, W = [int(x) for x in input().split()]

gs = []
for _ in range(N):
    gs.append(tuple(int(x) for x in input().split()))

gs.sort(key=lambda x: x[0] / x[1], reverse=True)

v = 0
w = 0
for gv , gw in gs:
    if (W - w) >= gw:
        v += gv
        w += gw
    else:
        v += gv * (W - w) / gw
        break

print(v)