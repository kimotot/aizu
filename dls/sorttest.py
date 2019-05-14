from random import randint

MAX = 1000

class Node:

    def __init__(self, n):
        self.data = n


def bubblesort(buff):
    n = len(buff)
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            if buff[j-1].data > buff[j].data:
                temp = buff[j-1]
                buff[j-1] = buff[j]
                buff[j] = temp

def quicksort(left, right, buff):
    i = left
    j = right
    pivot = (left + right) // 2
    p = buff[pivot].data
    while True:
        while buff[i].data <= p:
            i += 1
        while buff[j].data >= p:
            j -= 1

        if i >= j:
            if left
        else:
            temp = buff[i]
            buff[i] = buff[j]
            buff[j] = temp
            i += 1
            j -= 1




def debugdisp(buff):
    for node in buff:
        print(node.data, end = " ")
    print("")


if __name__ == "__main__":

    buff = [Node(randint(0, MAX * 10)) for _ in range(MAX)]
    debugdisp(buff)
    bubblesort(buff)
    debugdisp(buff)