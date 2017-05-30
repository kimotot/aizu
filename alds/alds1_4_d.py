def decode():
    [n, k] = [int(x) for x in input().split(" ")]
    ws = []
    for _ in range(n):
        ws.append(int(input()))

    return n, k, ws


def check(k, ws, p):
    sum_w = ws[0]
    tr = 1

    for w in ws[1:]:
        if sum_w + w <= p:
            sum_w += w
        else:
            sum_w = w
            tr += 1

            if tr > k:
                return False

    return True


if __name__ == '__main__':
    n, k, ws = decode()

    lo = max(ws)
    hi = sum(ws)

    while lo <= hi:
        p = (lo + hi) // 2

        if check(k, ws, p):
            hi = p - 1
            ans = p
        else:
            lo = p + 1

    print(ans)