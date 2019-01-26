# -*- coding: utf-8 -*-
import numpy as np

"""
This function finds the unique letters, and count their repetitions
and return the combined string containing letter followed by repetitions.
Example:
    print(processStrings('EEaaLbbccddXXL')
Result:
    'E2a2L2b2c2d2X2'
"""
def processStrings(str1):
    """A function to check repetition in the strings"""
    #set_alpha = set(str1)
    #set_alpha = sorted(list(set_alpha))
    set_alpha = []
    for letter in str1:
        if letter not in set_alpha:
            set_alpha.append(letter)
    zeros_for_dict = np.zeros(set_alpha.__len__(),dtype=int)
    dict_alpha = dict(zip(set_alpha, zeros_for_dict))
    for alpha in str1:
        if alpha in set_alpha:
            dict_alpha[alpha] += 1
    finalstr = ''.join("{!s}{!r}".format(key,val) for (key,val) in dict_alpha.items())
    return finalstr

if __name__ == '__main__':
    demo_string = 'aabbccddeeEEFFggg'
    print(processStrings(demo_string))