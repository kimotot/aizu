import math

count = 0

def insertionsort(a, n, g):
    global count

    for i in range(g, n):
        v = a[i]
        j = i -g
        while j >= 0 and a[j] > v:
            a[j + g] = a[j]
            j -= g
            count += 1
        a[j + g] = v


def shellsort(a, n):
    global count
    count = 0
    gs = []
    g = math.ceil(n / 2)
    while g > 1:
        gs.append(g)
        g = math.ceil(g / 2)
    gs.append(1)

    for g in gs:
        insertionsort(a, n, g)

    return a, gs


if __name__ == '__main__':

    n = int(input())
    a = []
    for _ in range(n):
        a.append(int(input()))

    a, gs = shellsort(a, len(a))

    print(len(gs))
    print(" ".join([str(x) for x in gs]))
    print(count)
    for i in a:
        print(i)