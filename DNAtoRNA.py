# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:37:39 2016

@author: james
"""

# DNA to RNA transcription

file = open('rosalind_rna.txt')

string = file.readline()
new = ''

for letter in string:
    if letter == 'T':
        new += 'U'
    else:
        new += letter
        
print(new)