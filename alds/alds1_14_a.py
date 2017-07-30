t = input()
p = input()

idx = t.find(p, 0)

while idx != -1:
    print(idx)
    idx = t.find(p, idx + 1)
