n = int(input())

coins = [25, 10, 5, 1]

ans = 0

for c in coins:
    tmp = n // c
    n = n - tmp * c
    ans += tmp

print(ans)
