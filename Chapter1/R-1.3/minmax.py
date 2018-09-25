# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 17:27:59 2018

@author: sangeeth.kalappu
"""

def minmax(list_):
    '''
    Function to find min and max in a sequence
    
    input  : list_ (a list of integers)
    output : (min_,max_)  (a tuple with min and max values)
    '''
    
    for key,value in enumerate(list_):
        if key == 0:
            min_ = value
            max_ = value
            continue
        
        if value > max_:
            max_ = value
            
        if min_ > value:
            min_ = value
        
    return (min_,max_)

if __name__ == '__main__':
    
    print("Enter numbers with space in between:")
    
    list_ = [int(num) for num in input().split(" ")]    
    min_,max_ = minmax(list_)
    
    print("Minimum : {0}\nMaximum : {1}".format(min_,max_))
