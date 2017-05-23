s = input().strip().split(" ")

[w, h, x, y, r] = [int(x) for x in s]

if (r <= x <= w-r) and (r <= y <= h-r):
    print("Yes")
else:
    print("No")
