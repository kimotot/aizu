f = {}


def fibo(n):
    global f
    if n == 0 or n == 1:
        return 1
    else:
        if n in f:
            return f[n]
        else:
            ans = fibo(n-1) + fibo(n-2)
            f[n] = ans
            return ans


n = int(input())
print(fibo(n))