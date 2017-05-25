[n, m, l] = [int(x) for x in input().split(" ")]
a = []
for _ in range(n):
    a.append([int(x) for x in input().split(" ")])

b = []
for _ in range(m):
    b.append([int(x) for x in input().split(" ")])

c = []
for i in range(n):
    t = []
    for j in range(l):
        s = 0
        for k in range(m):
            s += a[i][k] * b[k][j]
        t.append(s)
    c.append(t)

for arow in c:
    print(" ".join([str(x) for x in arow]))