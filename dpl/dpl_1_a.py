INF = 100000

n, m = map(int, input().split())
coins = [int(x) for x in input().split()]
coins.sort()

dp = [[0] * (n + 1) for _ in range(m)]
for i in range(n + 1):
    dp[0][i] = i


for j in range(1, m):
    c = coins[j]
    for i in range(1, n + 1):
        min_count = INF
        for mm in range(i // c + 1):
            amari = i - mm * c
            if dp[j - 1][amari] + mm < min_count:
                min_count = dp[j - 1][amari] + mm
        dp[j][i] = min_count

print(dp[m - 1][n])