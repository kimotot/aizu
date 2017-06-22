def findlcs(x, y):
    dp = [0] * (len(y) + 1)

    for c in x:
        tmp = dp[:]
        for j in range(len(y)):
            if c == y[j]:
                dp[j + 1] = tmp[j] + 1
            elif dp[j + 1] < dp[j]:
                dp[j + 1] = dp[j]

    return dp[-1]


q = int(input())
for k in range(q):
    X = input()
    Y = input()
    print(findlcs(X, Y))