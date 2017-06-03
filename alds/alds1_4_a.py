n = int(input())
s = [int(x) for x in input().strip().split(" ")]

q = int(input())
t = [int(x) for x in input().strip().split(" ")]

count = 0
for i in t:
    if i in s:
        count += 1

print(count)