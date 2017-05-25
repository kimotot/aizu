def gcm(a, b):

    if a % b == 0:
        return b
    else:
        return gcm(b, a % b)


if __name__ == '__main__':

    [a, b] = [int(x) for x in input().split()]

    print(gcm(a,b))