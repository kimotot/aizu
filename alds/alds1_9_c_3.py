import heapq

heap = []

while True:

    inst = input()
    if inst[0] == "i":
        heapq.heappush(heap, -int(inst[7:]))
    elif inst[1] == "x":
        print(-heapq.heappop(heap))
    else:
        break
