def lcs(x, y, i, j, t):
    if t[i][j] is not None:
        return t[i][j]
    elif i == 0 or j == 0:
        t[i][j] = 0
        return 0
    elif x[i-1] == y[j-1]:
        tmp = lcs(x, y, i-1, j-1, t) + 1
        t[i][j] = tmp
        return tmp
    else:
        tmp1 = lcs(x, y, i, j-1, t)
        tmp2 = lcs(x, y, i-1, j, t)
        tmp = max(tmp1, tmp2)
        t[i][j] = tmp
        return tmp

if __name__ == '__main__':

    q = int(input())
    for _ in range(q):
        x = input()
        y = input()
        t = [[None] * (len(y)+1) for _ in range(len(x)+1)]
        print(lcs(x, y, len(x), len(y), t))
