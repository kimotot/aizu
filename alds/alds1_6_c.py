def decode():
    n = int(input())
    cards = []
    for i in range(n):
        [m, v] = input().split()
        cards.append((m, int(v), i))

    return n, cards


def partition(a, p, r):
    x = a[r][1]
    i = p - 1

    for j in range(p, r):
        if a[j][1] <= x:
            i += 1
            t = a[j]
            a[j] = a[i]
            a[i] = t
    t = a[i+1]
    a[i+1] = a[r]
    a[r] = t

    return i+1


def disp(cards):
    for (m, n, _) in cards:
        print("{0} {1}".format(m, n))


def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q-1)
        quicksort(a, q+1, r)


def isstable(cards):
    for i in range(len(cards) - 1):
        if cards[i][1] == cards[i+1][1]:
            if cards[i][2] < cards[i+1][2]:
                pass
            else:
                return False
    return True

if __name__ == '__main__':
    n, cards = decode()

    quicksort(cards, 0, n-1)

    if isstable(cards):
        print("Stable")
    else:
        print("Not stable")

    disp(cards)
