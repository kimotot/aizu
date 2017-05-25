def insertSort(a):
    for i in range(len(a)):
        v = a[i]
        j = i - 1

        while j >= 0 and a[j] > v:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = v

        print(" ".join([str(x) for x in a]))

if __name__ == '__main__':

    n = int(input())
    a = [int(x) for x in input().split()]

    insertSort(a)


