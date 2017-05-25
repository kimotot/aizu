tscore = hscore = 0

n = int(input())
for _ in range(n):
    al = input().split()
    if al[0] > al[1]:
        tscore += 3
    elif al[0] < al[1]:
        hscore += 3
    else:
        tscore += 1
        hscore += 1

print(tscore, hscore)