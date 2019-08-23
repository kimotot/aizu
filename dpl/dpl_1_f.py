import bisect

INF = 10 ** 9 + 1
N, W = map(int, input().split())
V = N * 100

dp = [INF] * (V + 1)
dp[0] = 0
sum_v = 0
for _ in range(N):
    v, w = map(int, input().split())
    sum_v += v
    for i in range(sum_v, - 1, -1):
        dp[i] = min(dp[i], w + (dp[i - v] if i - v >= 0 else 0))

print(bisect.bisect_right(dp, W) - 1)
