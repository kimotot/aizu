s = input().strip().split(" ")
[a, b, c] = [int(x) for x in s]

if a < b < c:
    print("Yes")
else:
    print("No")