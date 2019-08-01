n = int(input())
A = [int(x) for x in input().split()]

x = A[0]
u = [x]

for a in A[1:]:
    if x == a:
        pass
    else:
        x = a
        u.append(x)

print(" ".join([str(x) for x in u]))