# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 17:46:59 2018

@author: sangeeth.kalappu
"""

import unittest
from sum_of_square import sum_of_square

class TestSumofSquare(unittest.TestCase):
    
    def test_datatype(self):
        res = sum_of_square([1,3,5,7,9])
        self.assertEqual(res,165)
        
if __name__ == "__main__":
    unittest.main()
    
