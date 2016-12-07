#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 21:55:43 2016

@author: james
"""

file = open('rosalind_subs.txt')

toRead = file.readline()
toFind = file.readline()

answer=[]
count=0

for i in range(len(toRead) - len(toFind)+1):
    #print(toRead[i:i+len(toFind)-1])
    #print(toFind[:-1])
    #print(i)
    if(toRead[i:i+len(toFind)-1] == toFind[:-1]):
        #print('hit')
        answer.append(i+1)
        count+=1
print(' '.join(str(x) for x in answer))
print(count)
#print(toRead[2-1:2-1+len(toFind)-1])