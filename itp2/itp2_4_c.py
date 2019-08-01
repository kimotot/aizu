n = int(input())
A = [int(x) for x in input().split()]

q = int(input())
for _ in range(q):
    [b, e, t] = [int(x) for x in input().split()]
    for k in range(e - b):
        tmp = A[b + k]
        A[b + k] = A[t + k]
        A[t + k] = tmp

print(" ".join([str(x) for x in A]))