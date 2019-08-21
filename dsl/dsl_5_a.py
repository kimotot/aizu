N, T = map(int, input().split())

rec = []
for _ in range(N):
    l, r = map(int, input().split())
    rec.append((l, 1))
    rec.append((r, -1))

rec.sort(key=lambda x: x[1])
rec.sort(key=lambda x: x[0])

max_c = 0
c = 0
for a in rec:
    c += a[1]
    if c > max_c:
        max_c = c

print(max_c)