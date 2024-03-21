#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictonary is None:
        return 'None'
    ans = 0
    ans2 = 0
    for key, value in a_dictionary.items():
        if value > ans:
            ans = value
            ans2 = key
    if ans == 0:
        return 'None'
    else:
        return ans2
