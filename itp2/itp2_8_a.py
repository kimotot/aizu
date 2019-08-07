q = int(input())
M = dict()

for _ in range(q):
    query = input().split()
    if query[0] == "0":
        M[query[1]] = int(query[2])
    else:
        print(M[query[1]])