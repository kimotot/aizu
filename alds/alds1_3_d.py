def decode():
    s = input()

    m = [0]
    h = 0
    for c in s:
        if c == "\\":
            h -= 1
        elif c == "_":
            pass
        else:
            h += 1

        m.append(h)

    return m


def checkwater(m, left):
    if m[left] <= m[left+1]:
        return False, 0, 0
    else:
        left_h = m[left]
        water = 0
        r = left + 1
        while r < len(m):
            if m[r] == m[r-1]:
                water += left_h - m[r]
            elif m[r] <= m[r-1]:
                water += left_h - m[r] - 0.5
            else:
                water += left_h - m[r] + 0.5

            if m[r] == left_h:
                return True, r, water

            r += 1

        return False, 0, 0


if __name__ == '__main__':

    def t():
        m = decode()
        print(m)
        left = int(input())
        result, r, water = checkwater(m, left)
        print(result, r, water)


    def main():
        m = decode()

        wlist = []
        left = 0
        while left < len(m) - 1:
            result, r, water = checkwater(m, left)
            if result:
                wlist.append(water)
                left = r
            else:
                left += 1

        print(int(sum(wlist)))
        wlist.insert(0, len(wlist))
        print(" ".join([str(int(x)) for x in wlist]))

    main()