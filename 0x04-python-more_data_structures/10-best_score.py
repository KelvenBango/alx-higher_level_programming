#!/usr/bin/python3

def best_score(a_dictionary):
    max = 0
    name = ""
    if a_dictionary is not None:
        for k, v in a_dictionary.items():
            if v >= max:
                max = v
                name = k
        return name
    else:
        return None
