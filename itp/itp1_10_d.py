import math

def dp1(xv, yv):
    d = 0.0
    for x, y in zip(xv, yv):
        d += abs(x - y)

    return d


def dp2(xv, yv):
    d = 0.0
    for x, y in zip(xv, yv):
        d += (x - y) ** 2

    d = math.sqrt(d)

    return d


def dp3(xv, yv):
    d = 0.0
    for x, y in zip(xv, yv):
        d += (abs(x - y)) ** 3

    d = math.pow(d, 1.0/3.0)

    return d


def dp8(xv, yv):
    d = 0.0
    for x, y in zip(xv, yv):
        if abs(x - y) > d:
            d = abs(x - y)

    return float(d)


if __name__ == '__main__':

    n = int(input())
    xv = [int(x) for x in input().split()]
    yv = [int(x) for x in input().split()]

    print(dp1(xv, yv))
    print(dp2(xv, yv))
    print(dp3(xv, yv))
    print(dp8(xv, yv))