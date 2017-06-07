from collections import deque

n = int(input())
dq = deque([])
for _ in range(n):
    L = input().split()
    if L[0] == 'insert':
        dq.appendleft(L[1])
    elif L[0] == 'delete':
        if L[1] in dq: dq.remove(L[1])
    elif L[0] == 'deleteFirst':
        dq.popleft()
    else:
        dq.pop()

print(' '.join(dq))