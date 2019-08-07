q = int(input())
M = dict()

for _ in range(q):
    query = input().split()
    if query[0] == "0":
        M[query[1]] = int(query[2])
    elif query[0] == "1":
        print(M.get(query[1], 0))
    elif query[0] == "2":
        if query[1] in M:
            del M[query[1]]
    else:
        d = sorted(M.items(), key=lambda x: x[0])
