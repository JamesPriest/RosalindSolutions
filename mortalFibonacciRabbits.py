#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 23:52:48 2016

@author: james
"""

file = open('rosalind_fibd.txt')

info=file.readline()
info=info.split(' ')

d={}
n,m=int(info[0]),int(info[1])
k=n
for i in range(1,m+1):
    d[i]=0
d[1]=1    

while n>1:
    #print(d)
    j=m
    temp=sum([d[x] for x in range(2,m+1)])
    while j!=0:
        d[j+1]=d[j]
        j-=1 
    d[1]=temp
    n-=1
if(k<m):
    print(sum([d[x] for x in range(1,k+1)]))
else:
    print(sum([d[x]for x in range(1,m+1)]))

'''for i in range(1,m+1):
    d[i]=0
d[1]=1
while n>2:
    print(d)
    j=m
    while j!=0:
        d[j+1]=d[j]
        j-=1
    d[j+1]=sum([d[x] for x in range(3,m+1)])
    n-=1    
print(d)
if(k<m):
    print(sum([d[x] for x in range(1,k+1)]))
else:
    print(sum([d[x]for x in range(1,m+1)]))'''