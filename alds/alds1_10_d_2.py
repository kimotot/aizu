import math
INF = math.inf


def calcdp():
    for j in range(1, N+1):
        for i in range(j, 0, -1):
            mn = INF
            for k in range(1, j-i+2):
                tmp = dp[i][j-k] + dp[j+2-k][j]
                if tmp < mn:
                    mn = tmp

            mn += pr[j] - pr[i - 1]
            mn += qr[j + 1] - qr[i - 1]

            dp[i][j] = mn


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
dp = [[0.0] * (N + 1) for _ in range(N + 2)]

for j in range(N+1):
    dp[j+1][j] = qc[j]

calcdp()

print(dp[1][N])