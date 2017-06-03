def decode():
    n = int(input())
    c = input().split()
    c = [(x[0], int(x[1])) for x in c]

    return n, c

def bubblesort(c):
    n = len(c)
    for i in range(n):
        for j in range(n-1, i, -1):
            if c[j][1] < c[j-1][1]:
                t = c[j-1]
                c[j-1] = c[j]
                c[j] = t
    return c


def selectionsort(c):
    n = len(c)

    for i in range(n):
        minj = i
        for j in range(i, n):
            if c[j][1] < c[minj][1]:
                minj = j

        if i != minj:
            t = c[i]
            c[i] = c[minj]
            c[minj] = t

    return c


def disp(c):
    strc = [x[0]+str(x[1]) for x in c]
    print(" ".join(strc))


def isstable(c1, c2):
    for i in range(1, 10):
        sc1 = list(filter(lambda x: x[1] == i, c1))
        sc2 = list(filter(lambda x: x[1] == i, c2))
        if sc1 == sc2:
            pass
        else:
            return False
    return True


if __name__ == '__main__':

    n, c = decode()

    c1 = list(c)
    c1 = bubblesort(c1)
    disp(c1)
    if isstable(c, c1):
        print("Stable")
    else:
        print("Not stable")

    c2 = list(c)
    c2 = selectionsort(c2)
    disp(c2)
    if isstable(c, c2):
        print("Stable")
    else:
        print("Not stable")

