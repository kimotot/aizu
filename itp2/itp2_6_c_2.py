n = int(input())
A = [int(x) for x in input().split()]

q = int(input())
for _ in range(q):
    k = int(input())

    ansl = n
    ansu = n

    anslf = False
    ansuf = False

    i = 0
    while (not anslf or not ansuf) and i < n:
        if not anslf and A[i] >= k:
            ansl = i
            anslf = True

        if not ansuf and A[i] > k:
            ansu = i
            ansuf = True

        i += 1

    print(ansl, ansu)
