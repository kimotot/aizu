
def shuffle(cards, h):
    return cards[h:] + cards[:h]

cards = ""
s = input()

while True:
    if s == "-":
        break

    cards = s
    n = int(input())
    for _ in range(n):
        cards = shuffle(cards, int(input()))

    print(cards)
    s = input()

