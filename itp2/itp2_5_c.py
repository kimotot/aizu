def dec(p, k, c):
    t = p[k]
    ltt = list(filter(lambda x: x < t, c))
    if ltt:
        new_t = max(ltt)
        c.remove(new_t)
        c.append(t)
        p[k] = new_t
        return p, c
    else:
        if k == 0:
            return None, c
        else:
            c.append(p[k])
            p, c = dec(p, k - 1, c)
            if p is None:
                return p, c
            else:
                p[k] = max(c)
                c.remove(p[k])
                return p, c

def inc(p, k, c):
    t = p[k]
    ltt = list(filter(lambda x: x > t, c))
    if ltt:
        new_t = min(ltt)
        c.remove(new_t)
        c.append(t)
        p[k] = new_t
        return p, c
    else:
        if k == 0:
            return None, c
        else:
            c.append(p[k])
            p, c = inc(p, k - 1, c)
            if p is None:
                return p, c
            else:
                p[k] = min(c)
                c.remove(p[k])
                return p, c

n = int(input())
A = [int(x) for x in input().split()]
p, c = dec(A[:], n - 1, [])
if p is not None:
    print(*p)

print(*A)

p, c = inc(A[:], n - 1, [])
if p is not None:
    print(*p)


