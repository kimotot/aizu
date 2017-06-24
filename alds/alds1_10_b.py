cost = None
r = None


def decode():
    n = int(input())

    for i in range(n):
        al = [int(x) for x in input().split()]
        if i == 0:
            r = list(al)
        else:
            r.append(al[1])

    return n, r


def get_min_cost(i, j):
    global cost, r

    if cost[i][j] is not None:
        return cost[i][j]
    elif i == j:
        cost[i][j] = 0
        return 0
    else:
        min_cost = None
        for k in range(i, j):
            tmp = get_min_cost(i, k) + get_min_cost(k+1, j) + r[i] * r[k+1] * r[j+1]
            if min_cost is None or tmp < min_cost:
                min_cost = tmp
        cost[i][j] = min_cost
        return min_cost


if __name__ == '__main__':

    n, r = decode()
    cost = [[None] * n for _ in range(n)]
    print(get_min_cost(0, n-1))