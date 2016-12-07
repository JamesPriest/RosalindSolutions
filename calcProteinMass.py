#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 21:29:42 2016

@author: james
"""

import massTableConversion as mtc

file = open('rosalind_prtm.txt').readline()

sumTot = 0

for i in file:
    if(i=='\n'):
        break
    print(i)
    sumTot+=float(mtc.d[i])
    
print(sumTot)
