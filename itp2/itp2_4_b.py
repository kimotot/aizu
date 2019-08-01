n = int(input())
A = [int(x) for x in input().split()]

q = int(input())
for _ in range(q):
    R = A[:]
    [b, m, e] = [int(x) for x in input().split()]
    for k in range(e - b):
        R[b + ((k + (e - m)) % (e - b))] = A[b + k]
    A = R[:]

print(" ".join([str(x) for x in A]))