INF = 100000

n, m = map(int, input().split())
coins = [int(x) for x in input().split()]
coins.sort()

dp = [x for x in range(n + 1)]
for i in range(n + 1):
    for mm in coins:
        if i + mm <= n and dp[i + mm] > dp[i] + 1:
            dp[i + mm] = dp[i] + 1

print(dp[n])