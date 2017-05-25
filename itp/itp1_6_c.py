array = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(4)]

n = int(input())
for _ in range(n):
    [b, f, r, v] = [int(x) for x in input().split(" ")]
    array[b-1][f-1][r-1] += v

for i, bl in enumerate(array):
    if i != 0:
        print("#" * 20)
    for fl in bl:
        print(" " + " ".join([str(x) for x in fl]))
