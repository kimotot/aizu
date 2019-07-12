import math
INF = math.inf


def calcdp(i, j):
    if i > j:
        return qc[i - 1]

    if dp[i][j] is not None:
        return dp[i][j]

    mn = INF

    for k in range(i, j + 1):
        tmp = calcdp(i, k - 1) + calcdp(k + 1, j)
        if tmp < mn:
            mn = tmp

    mn += pr[j] - pr[i - 1]
    mn += qr[j + 1] - qr[i - 1]

    dp[i][j] = mn
    return mn


# 要素数Nと書く要素の検索確率を読み込む
N = int(input())
pc = [float(x) for x in input().split()]
qc = [float(x) for x in input().split()]

# 要素の累積和を計算しておく
pr =[0.0]
for x in pc:
    pr.append(x + pr[-1])

qr = [0.0]
for x in qc:
    qr.append(x + qr[-1])


# 動的計画テーブルを初期化する
dp = [[None] * (N + 1) for _ in range(N + 1)]

print(calcdp(1, N))