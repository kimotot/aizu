def check(aline):
    pools = []
    leftedge = []

    for i, c in enumerate(aline):
        if c == "\\":
            leftedge.append(i)
        elif c == "_":
            pass
        else:
            if leftedge:
                left = leftedge.pop()
                w = i - left

                while pools and left < pools[-1][0]:
                    w += pools.pop()[1]

                pools.append((left, w))

    return pools


if __name__ == '__main__':

    al = input().strip()
    ps = check(al)

    print(sum([x[1] for x in ps]))
    print(len(ps), *[x[1] for x in ps])
