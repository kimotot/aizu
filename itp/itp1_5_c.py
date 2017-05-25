def decode():
    hws = []

    while True:
        [h, w] = [int(x) for x in input().strip().split(" ")]
        if h == w == 0:
            return hws
        else:
            hws.append((h, w))


def disprect(hw):

    def dispaline(x, first, second):
        for i in range(x):
            if i % 2 == 0:
                print(first, end="")
            else:
                print(second, end="")
        print("")


    (h, w) = hw

    for y in range(h):
        if y % 2 == 0:
            dispaline(w, "#", ".")
        else:
            dispaline(w, ".", "#")
    print("")


if __name__ == '__main__':
    hws = decode()
    for hw in hws:
        disprect(hw)