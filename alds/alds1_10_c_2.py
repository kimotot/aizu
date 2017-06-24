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


def make_table(x, y):
    t = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]

    for i in range(len(x) + 1):
        for j in range(len(y) + 1):
            if i == 0 or j == 0:
                pass
            elif x[i-1] == y[j-1]:
                t[i][j] = t[i-1][j-1] + 1
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])
    return t

if __name__ == '__main__':

    q = int(input())
    for _ in range(q):
        x = input()
        y = input()
        t = make_table(x, y)
        print(t[len(x)][len(y)])