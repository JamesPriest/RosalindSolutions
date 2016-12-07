w#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 14:55:31 2016

@author: james
"""

file=open('rosalind_gc.txt')

bigList=[]
translate='a'

while( translate != ""):
    translate=file.readline()
    bigList.append(translate)


l1=['A','C','T','G']

names=[]
content=[]
i=0

while True:
    count=0
    GC=0
    info=bigList[i]
    if(info==""):
        print('done')
        break
    i+=1
    string=bigList[i]
    while( string[0] != '>' ):
        for j in string:
            if( j in l1 ):
                count+=1
                #print(i + "hit!")
                if( j == 'G' or j == 'C' ):
                    GC+=1
        i+=1
        string=bigList[i] 
        if(bigList[i] == ""):
            break      
    info=info[1:]
    names.append(info)
    content.append(GC/count)
    info = string
    
#print(names)
#print(content)

chosen=0

for i in range(len(content)):
    if(content[i]>content[chosen]):
        chosen=i

print(names[chosen][:-1])
print(content[chosen]*100)