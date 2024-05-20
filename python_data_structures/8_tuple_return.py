#!/usr/bin/python3
list_ = [1, 2, 3, 4, 5]

def tuple_return(list_example):
    leng= len(list_example)
    if len(list_example) == 0:
        return (leng, None)
    else:
        return (leng, list_example[0])


result = tuple_return(list_)
print(result)
list_len, first_element = tuple_return(list_)
print(f"List len = {list_len}\nFirst element = {first_element}")
