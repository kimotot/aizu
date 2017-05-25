while True:
    s = input().strip().split(" ")
    [x, y] = [int(x) for x in s]

    if x == y == 0:
        break
    else:
        if x <= y:
            print(x,y)
        else:
            print(y,x)