# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 10:41:37 2016

@author: james
"""

infile = open('rosalind_ini4.txt')
a = infile.readline()
a = a.split(' ')

print( sum([x for x in range(int(a[0]),int(a[1])) if x % 2 == 1]))

