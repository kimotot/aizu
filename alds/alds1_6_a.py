def countingsort(a, k):
    n = len(a)
    c = [0] * (k+1)
    b = [0] * (n+1)

    for v in a:
        c[v] += 1

    for i in range(1, k+1):
        c[i] = c[i] + c[i-1]

    for j in range(len(a)-1, -1, -1):
        b[c[a[j]]] = a[j]
        c[a[j]] -= 1

    b.pop(0)
    return b


if __name__ == '__main__':

    n = int(input())
    a = [int(x) for x in input().split()]

    b = countingsort(a, 10000)

    print(" ".join([str(x) for x in b]))