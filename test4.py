# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 10:51:35 2016

@author: james
"""

infile = open('rosalind_ini5.txt')

string = infile.readlines()

print(''.join(string[1::2]))
