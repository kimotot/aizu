n = int(input())
A = [int(x) for x in input().split()]
m = int(input())
B = [int(x) for x in input().split()]

i = j = 0
while i < n and j < m:
    if A[i] == B[j]:
        print(A[i])
        i += 1
        j += 1
    elif A[i] < B[j]:
        i += 1
    else:
        j += 1
