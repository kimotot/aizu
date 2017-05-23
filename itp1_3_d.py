s = input().strip().split(" ")
[a, b, c] = [int(x) for x in s]

n = 0
for i in range(a, b +1):
    if c % i == 0:
        n += 1

print(n)