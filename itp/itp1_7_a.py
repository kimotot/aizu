while True:
    [m, f, r] = [int(x) for x in input().split(" ")]
    if m == f == r == -1:
        break

    result = ""
    s = m + f
    if m == -1 or f == -1:
        result = "F"
    elif s >= 80:
        result = "A"
    elif 65 <= s < 80:
        result = "B"
    elif 50 <= s < 65:
        result = "C"
    elif 30 <= s < 50:
        if r >= 50:
            result = "C"
        else:
            result = "D"
    elif s < 30:
        result = "F"

    print(result)