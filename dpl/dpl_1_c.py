N, W = map(int, input().split())
goods = []
for _ in range(N):
    goods.append([int(x) for x in input().split()])

dp = [[0] * (W + 1) for _ in range(N + 1)]

for n in range(1, N + 1):
    for w in range(W + 1):
        gv, gw = goods[n - 1]
        t = 0
        while w - gw * t >= 0:
            dp[n][w] = max(dp[n][w], dp[n -1][w - gw * t] + gv * t)
            t += 1

print(dp[N][W])
