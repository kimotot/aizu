def decode():
    n = int(input())
    a = [int(x) for x in input().split()]

    return n, a


def partition(a, p, r):
    x = a[r]
    i = p - 1

    for j in range(p, r):
        if a[j] <= x:
            i += 1
            t = a[j]
            a[j] = a[i]
            a[i] = t
    t = a[i+1]
    a[i+1] = a[r]
    a[r] = t

    return i+1


def disp(a, i):
    s = []
    for idx, v in enumerate(a):
        if idx == i:
            s.append("[" + str(v) + "]")
        else:
            s.append(str(v))

    print(" ".join(s))


if __name__ == '__main__':

    n, a = decode()
    i = partition(a, 0, len(a) - 1)
    disp(a, i)