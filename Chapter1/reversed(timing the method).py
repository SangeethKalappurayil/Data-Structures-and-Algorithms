# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 12:10:12 2018

@author: sangeeth.kalappu
"""
"""
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing:
"""
import numpy as np
    
def reverse(list_): return list_[-1::-1]


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

short_list = np.arange(10) 
wrapped = wrapper(costly_func, short_list)
timeit.timeit(wrapped, number=1000)

def reverse1(mylist):
    for index in range(len(mylist) - 1, -1, -1):
        yield mylist[index]