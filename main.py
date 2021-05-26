import os
# count_line = 0
# count_file = 0
# list = 5
# print(list)
list = []
list_one = []
list_two = []
list_three = []


with open("1.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    name = "1.txt"
    count_line = str(len(lines))
    list_one.append(name)
    list_one.append(count_line)
    list_one.append(lines)

    # print(f"{name}\n{count_line}\n{lines}\n")
    # print(list_one)

with open("2.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    name = "2.txt"
    count_line = str(len(lines))
    list_two.append(name)
    list_two.append(count_line)
    list_two.append(lines)
    # print(f"{name}\n{count_line}\n{lines}\n")
    # print(list_two)

with open("3.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    name = "3.txt"
    count_line = len(lines)
    list_three.append(name)
    list_three.append(count_line)
    list_three.append(lines)
    # print(f"{name}\n{count_line}\n{lines}\n")
    # print(list_three)

list.append(list_one)
list.append(list_two)
list.append(list_three)
# print(sorted(list, key=len))

