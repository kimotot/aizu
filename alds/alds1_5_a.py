a = []
d = {}

def decode():
    global a

    n = int(input())
    a = [int(x) for x in input().split()]

    q = int(input())
    ms = [int(x) for x in input().split()]

    return n, a, q, ms


def solve(i, m):
    global a, d

    if (i, m) in d:
        return d[(i, m)]

    if a[i] == m:
        d[(i, m)] = True
        return True
    else:
        if i < len(a) - 1:

            if solve(i+1, m) or (m - a[i] > 0 and solve(i+1, m-a[i])):
                d[(i, m)] = True
                return True
            else:
                d[(i, m)] = False
                return False

        else:
            d[(i, m)] = False
            return False


if __name__ == '__main__':

    n, a, q, ms = decode()
    for m in ms:
        if solve(0, m):
            print("yes")
        else:
            print("no")

