# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 10:38:01 2016

@author: james
"""

infile = open('Lol.txt')
string1 = infile.readline()
string2 = infile.readline()
string2 = string2.split(' ')

print(int(string2[3]))