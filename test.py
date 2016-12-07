# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 18:42:43 2016

@author: james
"""

f = open('rosalind_ini3.txt')
line_number = 1
for lines in f:
    if line_number == 1:
        text = lines
        line_number += 1
    elif line_number == 2:
        places = lines

firstStart = int(places[0:2])
firstEnd = int(places[3:5])
secondStart = int(places[6:9])
secondEnd = int(places[10:13])

print(text[firstStart: firstEnd+1])
print(text[secondStart: secondEnd+1])