#!/usr/bin/python3
my_list = [5, 4, 3, 2, 1]
value = []
for i in range(0,len(my_list)):
    if my_list[i]%2:
        value.append(True)
    else:
        value.append(False)
print(my_list, '\n', tuple(value))
