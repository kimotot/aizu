while True:

    [a, op, b] = input().strip().split(" ")

    if op == "?":
        break

    a = int(a)
    b = int(b)

    if op == "+":
        f = lambda x, y: x + y
    elif op == "-":
        f = lambda x, y: x - y
    elif op == "*":
        f = lambda x, y: x * y
    else:
        f = lambda x, y: x // y

    print(f(a, b))

