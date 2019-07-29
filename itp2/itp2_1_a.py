q = int(input())
array = []

for _ in range(q):
    query = input()

    if query[0] == "0":       # pushBack
        array.append(int(query[2:]))
    elif query[0] == "1":     # randomAccess
        print(array[int(query[2:])])
    else:                   # popBack
        array.pop()
