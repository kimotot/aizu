cards = [(s, n) for s in "SHCD" for n in range(1, 14)]

n = int(input())
for _ in range(n):
    al = input().strip().split(" ")
    cards.remove((al[0], int(al[1])))

for (s, n) in cards:
    print(s, n)