n = int(input())

A = []
for _ in range(n):
    A.append(tuple(int(k) for k in input().split()))

A.sort(key= lambda k: k[1])
A.sort(key= lambda k: k[0])

for (x, y) in A:
    print(x, y)