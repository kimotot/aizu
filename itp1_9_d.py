def fprint(str, a, b):
    print(str[a:b+1])


def freverse(str, a, b):
    n_str = list(str)
    t = n_str[a: b+1]
    t.reverse()
    for i in range(b - a + 1):
        n_str[a + i] = t[i]
    return "".join(n_str)


def freplace(str, a, b, p):
    n_str = list(str)
    for i in range(b - a + 1):
        n_str[a + i] = p[i]
    return "".join(n_str)


str = input()
n = int(input())
for _ in range(n):
    al = input().split()
    if al[0] == "print":
        fprint(str, int(al[1]), int(al[2]))
    elif al[0] == "reverse":
        str = freverse(str, int(al[1]), int(al[2]))
    elif al[0] == "replace":
        str = freplace(str, int(al[1]), int(al[2]), al[3])
