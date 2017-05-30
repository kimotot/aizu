def bin_search(m, s, left, right):
    if left <= right:
        n = (left + right) // 2
        if s[n] == m:
            return True
        elif m < s[n]:
            return bin_search(m, s, left, n-1)
        else:
            return bin_search(m, s, n+1, right)


n = int(input())
s = [int(x) for x in input().strip().split(" ")]

q = int(input())
t = [int(x) for x in input().strip().split(" ")]

count = 0
for i in t:
    if bin_search(i, s, 0, len(s)-1):
        count += 1

print(count)