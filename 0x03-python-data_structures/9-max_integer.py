#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        ans = 0
        for i in my_list:
            if i > ans:
                ans = i
        return ans
