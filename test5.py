# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:02:54 2016

@author: james
"""

file = open('rosalind_ini6.txt')
string = file.readline()

# print(string)
dict = {}

for word in string.split(' '):
    word = word.rstrip('\n')
    # print(word)
    if not word in dict:
        dict[word] = 1
    else:
        dict[word] += 1

for key, value in dict.items():
    print(str(key) + ' ' + str(value))
    
