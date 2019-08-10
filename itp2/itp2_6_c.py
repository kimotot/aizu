def binsearch(left, right, k):
    global A

    while left < right:
        middle = (left + right) // 2
        if A[middle] < k:
            return binsearch(middle + 1, right, k)
        else:
            if middle == 0:
                return 0
            elif A[middle - 1] < k:
                return middle
            else:
                return binsearch(left, middle, k)

    return len(A)


def binsearch2(left, right, k):
    global A

    while left < right:
        middle = (left + right) // 2
        if A[middle] <= k:
            return binsearch2(middle + 1, right, k)
        else:
            if middle == 0:
                return 0
            elif A[middle - 1] <= k:
                return middle
            else:
                return binsearch2(left, middle, k)

    return len(A)


n = int(input())
A = [int(x) for x in input().split()]

q = int(input())
for _ in range(q):
    k = int(input())
    print(binsearch(0, n, k), binsearch2(0, n, k))

