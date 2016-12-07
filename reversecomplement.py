# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:45:51 2016

@author: james
"""

file = open('rosalind_revc.txt')

string = file.readline()

new = ''

for letter in string:
    if letter == 'A':
        new += 'T'
    elif letter == 'T':
        new += 'A'
    elif letter == 'C':
        new += 'G'
    elif letter == 'G':
        new += 'C'

print(new[::-1])         