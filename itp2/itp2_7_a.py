s = set()

q = int(input())
for _ in range(q):
    [i, x] = [int(k) for k in input().split()]
    if i == 0:
        s.add(x)
        print(len(s))
    else:
        if x in s:
            print(1)
        else:
            print(0)

