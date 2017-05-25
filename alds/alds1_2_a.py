def bubbleSort(a):
    flag = True
    count = 0
    i = 0
    while flag:
        flag = False
        for j in range(len(a)-1, i, -1):
            if a[j] < a[j -1]:
                t = a[j - 1]
                a[j - 1] = a[j]
                a[j] = t
                count += 1
                flag = True
        i += 1

    return count, a

if __name__ == '__main__':

    n = int(input())
    a = [int(x) for x in input().split()]

    c, a = bubbleSort(a)
    print(" ".join([str(x) for x in a]))
    print(c)