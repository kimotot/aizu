def decode():
    hws = []

    while True:
        [h, w] = [int(x) for x in input().strip().split(" ")]
        if h == w == 0:
            return hws
        else:
            hws.append((h, w))


def disprect(hw):
    (h, w) = hw

    print("#" * w)
    for _ in range(h - 2):
        print("#" + "." * (w-2) + "#")
    print("#" * w)
    print("")


if __name__ == '__main__':
    hws = decode()
    for hw in hws:
        disprect(hw)