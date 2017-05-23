n = int(input())

ans = []
for i in range(1, n+1):
    if i % 3 == 0:
        ans.append(i)
    else:
        s = str(i)
        if '3' in s:
            ans.append(i)

print(" " + " ".join([str(x) for x in ans]))