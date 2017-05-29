s = input().split()

stack = []
for i in s:
    if i.isdigit():
        stack.append(int(i))
    else:
        if i == "+":
            f = lambda x, y: x + y
        elif i == "-":
            f = lambda x, y: x - y
        elif i == "*":
            f = lambda x, y: x * y

        y = stack.pop()
        x = stack.pop()
        stack.append(f(x, y))

print(stack[0])
