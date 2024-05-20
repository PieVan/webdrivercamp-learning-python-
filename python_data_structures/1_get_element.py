#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = 2

def printRangeList(elements,index):
    if index in range(0, len(elements)):
        print(f"The element is {elements[index]}")
    else: return None

printRangeList(list_,index)
