#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 16:27:57 2016

@author: james
"""
file = open('rosalind_mer.txt')
junk=file.readline()
array1=[int(x) for x in file.readline().split(' ')]
junk=file.readline()
array2=[int(x) for x in file.readline().split(' ')]
        
l3=sorted(array1+array2)
l4=[str(x) for x in l3]
print(' '.join(l4))
