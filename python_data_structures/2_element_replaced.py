#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5

def prinSmt(list,index,element_to_replace)->[]:
    if index > len(list):
        print(list)
    else:
        list[index] = element_to_replace
        print(list)
prinSmt(list_,index,element_to_replace)
