
ALP = "abcdefghijklmnopqrstuvwxyz"
d = {key: 0 for key in ALP}

while True:
    try:
        s = input()
        for c in s.lower():
            if c.isalpha():
                d[c] += 1
    except EOFError:
        break

for c in ALP:
    print("{0:s} : {1:d}".format(c, d[c]))