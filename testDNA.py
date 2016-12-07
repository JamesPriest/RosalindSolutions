# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:27:51 2016

@author: james
"""

file = open('rosalind_dna.txt')

string = file.readline()
A,T,C,G = 0,0,0,0

for letter in string:
    if letter == 'A':
        A += 1
    elif letter == 'T':
        T += 1        
    elif letter == 'C':
        C += 1        
    elif letter == 'G':
        G += 1   

print(str(A) + ' ' + str(C) + ' ' + str(G) + ' ' + str(T))             