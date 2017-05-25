import math

while True:

    n = int(input())

    if n == 0:
        break

    st = [int(x) for x in input().split()]

    sum_st = sum(st)
    m = sum_st / n

    aa = 0
    for s in st:
        aa += (s-m)**2
    aa /= n

    print(math.sqrt(aa))