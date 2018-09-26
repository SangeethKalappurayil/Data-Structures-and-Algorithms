# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 13:12:36 2018

@author: sangeeth.kalappu
"""

"""
Write a short Python function that counts the number of vowels in a given
character string.
"""

def count_vowels(string):
    """
    Function counts number of vowels present
    in a given character string
    
    input : string
    output : count of vowels
    """
    
    if not(isinstance(string,str)):
        raise TypeError("The argument for 'count_vowels' function should be string.")
    count = 0
    for vowel in list('aeiou'):
        if vowel in string:
            count += 1
    
    return count
