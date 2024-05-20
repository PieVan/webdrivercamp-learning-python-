#!/usr/bin/python3

string = """AbraCadabra
A new string voila!"""

def remove_char(some_string):
    new_string=""
    for char in some_string:
        if char != 'a' and char != 'A':
            new_string += char
    print(new_string)

remove_char(string)
