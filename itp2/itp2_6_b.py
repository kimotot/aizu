n = int(input())
A = [int(x) for x in input().split()]

m = int(input())
B = [int(x) for x in input().split()]

i = 0
j = 0

while i < n and j < m:
    if A[i] == B[j]:
        i += 1
        j += 1
    elif A[i] < B[j]:
        i += 1
    else:
        break

if j == m and i <= n:
    print(1)
else:
    print(0)