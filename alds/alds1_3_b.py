[n, q] = [int(x) for x in input().split()]
qs = []
for _ in range(n):
    al = input().split()
    qs.append([al[0], int(al[1])])

t = 0
while len(qs) > 0:
    task = qs.pop(0)
    if task[1] <= q:
        t += task[1]
        print(task[0], t)
    else:
        t += q
        task[1] -= q
        qs.append(task)
