s = input().strip().split(" ")
number_list = [int(x) for x in s]

number_list.sort()
print(" ".join([str(x) for x in number_list]))