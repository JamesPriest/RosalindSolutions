# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 21:39:51 2016

@author: james
"""

import random

def interaction(a,b):
    # print(a + ' ' + b)
    if( a == 'A' and b == 'A' ):
       # print('Top1')
        return 'A'
    if( (a == 'A' and b == 'B') or (b == 'A' and a == 'B')):
       # print('Top2')
        if(random.random() <= 0.5):
            return 'A'
        else:
            return 'B'
    if( (a == 'A' and b == 'C') or (b == 'A' and a == 'C') ):
       # print('Top3')
        return 'B'
    if( a == 'B' and b == 'B' ):
       # print('Top4')
        j = random.random()   
        print("j is %f" % j)
        if( j <= 0.25 ):
            return 'A'
        elif( j <=0.75  ):
            return 'B'
        else:
            return 'C'
    if( (a == 'B' and b == 'C') or (b == 'B' and a == 'C') ):
        if( random.random() <= 0.50 ):
            print('Top5 - ret B')
            return 'B'
        else:
            print('Top5 - ret C')
            return 'C'
    if( a == 'C' and b == 'C' ):
       # print('Top6')
        return 'C'
      
# Sum together all possibility, and go k/total, m/total, n/total
# Sets each probability from interval
      
# Local variable setup
total = 0
Aresult, Bresult, Cresult = 0,0,0 

for i in range(0,4800000):
    i = random.random()
    j = random.random()
    if( i <= 1/3 ):
        i = 'A'
    elif(  i <= 2/3 ):
        i = 'B'
    else:
        i = 'C'  
        
    if( j <= 1/3 ):
        j = 'A'
    elif( j <= 2/3 ):
        j = 'B'
    else:
        j = 'C'
    
    print("i is " + i + ", j is " + j )
    total += 1
    result = interaction(i,j)
    print( result )
    if( result == 'A' ):
        Aresult += 1
    elif( result == 'B' ):
        Bresult += 1
    elif( result == 'C' ):
        Cresult += 1
    else:
       print("Failed" + " " + str(result) )

print( total/2 )
print( Aresult/2 )
print( Bresult/2 )
print( Cresult/2 )
print( (Aresult + Bresult)/total )