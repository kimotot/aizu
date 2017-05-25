while True:

    [n, x] = [int(x) for x in input().split(" ")]
    if n == x == 0:
        break

    ans = 0
    for i in range(1, n+1):
        if i >= x:
            break

        for j in range(i+1, n+1):
            if i+j >= x:
                break

            for k in range(j+1, n+1):
                if i+j+k > x:
                    break
                elif i+j+k == x:
                    ans += 1

    print(ans)