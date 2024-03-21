#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    ans = 0
    ans2 = None
    for key, value in a_dictionary.items():
        if value > ans:
            ans = value
            ans2 = key
    return ans2
