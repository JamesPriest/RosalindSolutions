#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 14:38:37 2016

@author: james
"""

def parRe(n):
    if(n == 0):
        return 1
    if(n == 1):
        return 2
    return 2*n*parRe(n-1)-(n-1)**2*parRe(n-2)
    
import itertools

l1 = ''.join([str for x in range(22)])
print(l1)
#itertools.permutations(l1,7)