# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:56:06 2016

@author: james
"""

file = open('rosalind_fib.txt')

for word in file:
    string = word.split(' ')

a = int(string[0])
b = int(string[1])

def fib(n,k):
    if n > 2:
        return fib(n-1,k) + k*fib(n-2,k)
    else:
        return 1
        
print(fib(a,b))