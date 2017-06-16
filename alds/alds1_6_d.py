def decode():
    n = int(input())
    w = [int(x) for x in input().split()]

    return n, w


def search(w, sw, swi):
    wi = w.index(sw[swi])
    cost = 0
    count = 0
    while wi != swi:
        tw = sw[wi]
        ti = w.index(tw)
        w[ti], w[wi] = w[wi], w[ti]
        cost += w[ti] + w[wi]
        count += 1
        wi = ti
    return cost, count


def search_min_cost(w):
    sorted_w = list(w)
    sorted_w.sort()

    min_w = sorted_w[0]
    cost = 0

    for i, sww in enumerate(sorted_w):
        tmp_cost, count = search(w, sorted_w, i)
        cost += min(tmp_cost, tmp_cost + (min_w + sww) * 2 - (sww - min_w) * count)

    return cost


if __name__ == '__main__':

    n, w = decode()
    print(search_min_cost(w))