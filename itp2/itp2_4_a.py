n = int(input())
A = [int(x) for x in input().split()]

q = int(input())
for _ in range(q):
    b, e = [int(x) for x in input().split()]
    B = A[b: e]
    B.reverse()
    A[b:e] = B

print(" ".join([str(x) for x in A]))