def syakutori():
    global A, N, S
    j = 0
    min_l = N + 1
    s = 0

    for i in range(N):
        while j < N and s < S:
            s += A[j]
            j += 1

        if s < S:
            break

        min_l = min(min_l, j - i)

        if i == j:
            j += 1
        else:
            s -= A[i]

    return min_l if min_l != N + 1 else 0


N, S = map(int, input().split())
A = [int(x) for x in input().split()]
print(syakutori())
