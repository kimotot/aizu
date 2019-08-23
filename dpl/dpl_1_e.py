INF = 1001

s1 = [c for c in input()]
s2 = [c for c in input()]

ls1 = len(s1)
ls2 = len(s2)

dp = [[INF] * (ls1 + 1) for _ in range(ls2 + 1)]
for i in range(ls1 + 1):
    dp[0][i] = i
for j in range(ls2 + 1):
    dp[j][0] = j

for j in range(1, ls2 + 1):
    for i in range(1, ls1 + 1):
        dp[j][i] = min(dp[j][i], dp[j][i - 1] + 1)
        dp[j][i] = min(dp[j][i], dp[j - 1][i] + 1)
        dp[j][i] = min(dp[j][i], dp[j - 1][i - 1] + (0 if s1[i - 1] == s2[j - 1] else 1))

print(dp[ls2][ls1])