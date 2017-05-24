while True:
    s = input()
    if s == "0":
        break

    print(sum([int(x) for x in s]))