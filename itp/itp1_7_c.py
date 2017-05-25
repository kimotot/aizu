[r, c] = [int(x) for x in input().split(" ")]
sheet = []
for _ in range(r):
    al = [int(x) for x in input().split(" ")]
    s = sum(al)
    al.append(s)
    sheet.append(al)

rl = [0] * (c+1)
for al in sheet:
    for i in range(c+1):
        rl[i] += al[i]
sheet.append(rl)

for al in sheet:
    print(" ".join([str(x) for x in al]))
