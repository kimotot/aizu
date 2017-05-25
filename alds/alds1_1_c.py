import math

def isprime(n):

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True


if __name__ == '__main__':

    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(int(input()))

    count = 0
    for n in nums:
        if isprime(n):
            count += 1

    print(count)