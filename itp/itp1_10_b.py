import math

[a, b, C] = [int(x) for x in input().split()]

c = math.sqrt(a*a + b*b - 2*a*b*math.cos(math.radians(C)))
L = a + b + c

h = b * math.sin(math.radians(C))

S = a * h / 2

print(S)
print(L)
print(h)