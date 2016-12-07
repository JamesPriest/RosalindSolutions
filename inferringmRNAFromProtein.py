#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 14:28:34 2016

@author: james
"""

import RNADictionary as RNA

info = RNA.giveDict()

file = open('rosalind_mrna.txt')
line = file.readline()

total=1
count=0

for j in line:
    print(j)
    if(j == ' '):
        j = 'STOP'
    for keys in info:
        if( info[keys] == j ):
            count+=1
    if(count != 0 ):
        total*=count
    count=0
    
print(total%1000000)