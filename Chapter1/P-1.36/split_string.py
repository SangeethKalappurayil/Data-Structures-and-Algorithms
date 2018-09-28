# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 15:43:35 2018

@author: sangeeth.kalappu
"""

"""
Write a Python program that inputs a list of words, separated by whitespace,
and outputs how many times each word appears in the list. You
need not worry about efficiency at this point, however, as this topic is
something that will be addressed later in this book.
"""

string = 'Write a Python program that inputs a list of words'

whitespace_index = [-1]
for index,value in enumerate(string):
    if value == ' ':
        whitespace_index.append(index)
        
whitespace_index.append(len(string))
        
word = []
for index,value in enumerate(whitespace_index[:-1]):
    temp = string[whitespace_index[index]+1:whitespace_index[index+1]]    
    word.append(temp)     
