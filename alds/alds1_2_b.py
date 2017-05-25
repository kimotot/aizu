def selectionSort(a):
    n = len(a)
    count = 0

    for i in range(n - 1):
        minj = i
        for j in range(i, n):
            if a[j] < a[minj]:
                minj = j

        if minj == i:
            pass
        else:
            t = a[i]
            a[i] = a[minj]
            a[minj] = t
            count += 1

    return a, count


if __name__ == '__main__':

    n = int(input())
    a = [int(x) for x in input().split()]

    a, c = selectionSort(a)

    print(" ".join([str(x) for x in a]))
    print(c)
