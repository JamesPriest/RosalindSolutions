#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 20:48:00 2016

@author: james
"""

file = open('rosalind_hamm.txt')

line1 = file.readline()
line2 = file.readline()
count=0

for i in range(len(line2)):
    if(line1[i] != line2[i]):
        count+=1
        
print(count)