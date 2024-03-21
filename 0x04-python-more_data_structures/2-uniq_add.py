#!/usr/bin/pyhton3
def uniq_add(my_list=[]):
    sum = 0
    new_set = set(my_list.copy())
    for i in new_set:
        sum += i
    return sum 
        


