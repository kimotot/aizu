N, W = map(int, input().split())
goods = []
for _ in range(N):
    goods.append([int(x) for x in input().split()])

dp = [[0] * (W + 1) for _ in range(N + 1)]

for n in range(1, N + 1):
    for w in range(W + 1):
        gv, gw = goods[n - 1]
        if w >= gw:
            dp[n][w] = max(dp[n -1][w], dp[n - 1][w - gw] + gv)
        else:
            dp[n][w] = dp[n - 1][w]

print(dp[N][W])
