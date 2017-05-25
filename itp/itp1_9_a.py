import re

w = input().lower()

s = 0
while True:
    line = input()
    if line == "END_OF_TEXT":
        break

    line = line.lower()
    splited_list = re.split(r'[ ,."]', line)

    s += splited_list.count(w)


print(s)