#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 00:41:42 2016

@author: james
"""

import itertools as it

file = open('rosalind_perm.txt')

n=int(file.readline())

l=[]

for i in range(1,n+1):
    l.append(str(i))
l1= [' '.join(x) for x in it.permutations("".join(l),n)]


file = open('results', 'a')

file.write(str(n!)+'\n')
for i in range(len(l1)):
    print(str(l1[i]))
    file.write(str(l1[i])+'\n')
