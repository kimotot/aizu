import bisect

INF = 10 ** 9 + 1

n = int(input())
dp = []

for _ in range(n):
    a = int(input())
    if len(dp) == 0 or dp[-1] < a:
        dp.append(a)
    else:
        dp[bisect.bisect_left(dp, a)] = a

print(len(dp))
