n = int(input())
s = input().strip().split(" ")
num_list = [int(x) for x in s]

print("{0:d} {1:d} {2:d}".format(min(num_list), max(num_list), sum(num_list)))