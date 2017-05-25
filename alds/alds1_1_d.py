def maxp(rs):
    maxv = rs[1] - rs[0]
    minv = rs[0]

    for j in range(1, len(rs)):
        if rs[j] - minv > maxv:
            maxv = rs[j] - minv
        if rs[j] < minv:
            minv = rs[j]

    return maxv

if __name__ == '__main__':

    n = int(input())
    rs = []
    for _ in range(n):
        rs.append(int(input()))

    print(maxp(rs))

