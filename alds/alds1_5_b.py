count = 0

def merge(a, left, mid, right):
    global count

    l = a[left:mid]
    r = a[mid:right]
    l.append(10**9+1)
    r.append(10**9+1)

    i = 0
    j = 0
    for k in range(left, right):
        count += 1
        if l[i] <= r[j]:
            a[k] = l[i]
            i += 1
        else:
            a[k] = r[j]
            j += 1


def mergeSort(a, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        mergeSort(a, left, mid)
        mergeSort(a, mid, right)
        merge(a, left, mid, right)


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]

    mergeSort(a, 0, n)

    print(*a)
    print(count)