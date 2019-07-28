N = int(input())

task = []
for _ in range(N):
    task.append(tuple(int(x) for x in input().split()))

task.sort(key=lambda x: x[1])
etime = 0
count = 0

for ts, te in task:
    if etime < ts:
        count += 1
        etime = te

print(count)