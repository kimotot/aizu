MASK = 2 ** 32 - 1
x = int(input())

print("{0:032b}".format(x))
print("{0:032b}".format(MASK - x))
print("{0:032b}".format((x << 1) & MASK))
print("{0:032b}".format(x >> 1))

