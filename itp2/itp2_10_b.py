MASK = 2 ** 32 - 1
a, b = map(int, input().split())

print("{0:032b}".format(a & b))
print("{0:032b}".format(a | b))
print("{0:032b}".format(a ^ b))

