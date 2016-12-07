#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:42:35 2016

@author: james
"""

def insertionSort(A):
    count=0
    for i in range(1, len(A)):
        k=i
        while(k>0 and A[k]<A[k-1]):
            count+=1
            temp=A[k]
            A[k]=A[k-1]
            A[k-1]=temp
            k=k-1
    print("count is %d" % count)
    return count
       
file = open('rosalind_ins.txt')

info = file.readline()
info = file.readline()

l1 = [int(x) for x in info.split(' ')]

#print(l1)

#A=[int(x) for x in '6 10 4 5 1 2'.split(' ')]

#print(A)
print(insertionSort(l1))