[a, b] = [int(x) for x in input().strip().split(" ")]

print("{0:d} {1:d} {2:f}".format(a // b, a % b, a / b))