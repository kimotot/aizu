def permutation(pre, other):
    if other:
        for a in other:
            new_pre = pre[:]
            new_pre.append(a)
            new_other = other[:]
            new_other.remove(a)
            permutation(new_pre, new_other)
    else:
        print(*pre)
    return


n = int(input())
permutation([], list(range(1, n+1)))


