def syakutori():
    global A, N, K
    checked = [0] * (K + 1)

    comp = 0
    j = 0
    min_l = N + 1

    for i in range(N):
        while j < N and comp < K:
            if A[j] <= K:
                if checked[A[j]] == 0:
                    comp += 1
                    checked[A[j]] = 1
                else:
                    checked[A[j]] += 1
            j += 1

        if comp < K:
            break

        min_l = min(min_l, j - i)

        if i == j:
            j += 1
        else:
            if A[i] <= K:
                if checked[A[i]] == 1:
                    comp -= 1
                    checked[A[i]] = 0
                else:
                    checked[A[i]] -= 1

    return min_l if min_l != N + 1 else 0


N, K = map(int, input().split())
A = [int(x) for x in input().split()]
print(syakutori())
