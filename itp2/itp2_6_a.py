def binsearch(left, right, k):
    global A

    while left < right:
        middle = (left + right) // 2
        if A[middle] == k:
            return True
        else:
            if A[middle] > k:
                right = middle
            else:
                left = middle + 1

    return False


n = int(input())
A = [int(x) for x in input().split()]

q = int(input())
for _ in range(q):
    k = int(input())
    if binsearch(0, n, k):
        print(1)
    else:
        print(0)
