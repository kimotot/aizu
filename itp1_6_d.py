[n, m] = [int(x) for x in input().split(" ")]

v1 = []
for _ in range(n):
    al = [int(x) for x in input().split(" ")]
    v1.append(al)

v2 = []
for _ in range(m):
    v2.append(int(input()))

v3 = []
for al in v1:
    t = 0
    for (a, b) in zip(al, v2):
        t += (a * b)
    v3.append(t)

for i in v3:
    print(i)
