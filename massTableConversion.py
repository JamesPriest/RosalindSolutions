#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 21:24:01 2016

@author: james
"""

file = open('monoisotopicMassTable')

d = dict(x.rstrip().split(None, 1) for x in file)
    
#print(d)