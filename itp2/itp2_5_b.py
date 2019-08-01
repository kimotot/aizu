n = int(input())

A = []
for _ in range(n):
    A.append(tuple(input().split()))

A.sort(key= lambda k: k[4])
A.sort(key= lambda k: int(k[3]))
A.sort(key= lambda k: k[2])
A.sort(key= lambda k: int(k[1]))
A.sort(key= lambda k: int(k[0]))

for g in A:
    print(" ".join(g))