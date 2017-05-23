s = input()

ans = []
for c in s:
    if c.islower():
        ans.append(c.upper())
    elif c.isupper():
        ans.append(c.lower())
    else:
        ans.append(c)

print("".join(ans))