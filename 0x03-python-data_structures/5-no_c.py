#!/usr/bin/python3
def no_c(my_string):
    ans = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            ans += i
    return ans
