#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 17:27:46 2020

@author: rgrimson
"""
#%%
import string
#%%
#Ejercicio 1
filename="palabras.txt"
fp = open(filename)
for line in fp:
    if len(line)>22:
        print(line)
#%%
#Ejercicio 2
def tiene(palabra, letra):
    return letra in palabra

tiene("pepeaAá",'a')
#%%
tot=0
cone=0
cona=0
coni=0
cono=0
conu=0
filename="palabras.txt"
fp = open(filename)
for line in fp:
    tot+=1
    if tiene(line,'a') or tiene(line,'á'):
        cona+=1
    if tiene(line,'e') or tiene(line,'é'):
        cone+=1
    if tiene(line,'i') or tiene(line,'í'):
        coni+=1
    if tiene(line,'o') or tiene(line,'ó'):
        cono+=1
    if tiene(line,'u') or tiene(line,'ú'):
        conu+=1
        
print("con A: ",cona/tot)
print("con E: ",cone/tot)
print("con I: ",coni/tot)
print("con O: ",cono/tot)
print("con U: ",conu/tot)
#%%
        
strippables = string.punctuation + string.whitespace
filename="AperturaSesiones2020.txt"
filename="LaudatoSi.txt"
#%%filename)
fp = open(filename)
hist={}
for line in fp:
    line = line.replace('-', ' ')

    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip(strippables)
        word = word.lower()

        # update the histogram
        hist[word] = hist.get(word, 0) + 1
#%%
for p in hist.keys():
    if hist[p]>20 and len(p)>4:
        print(p,hist[p])

#%%    
N=[]
for p in hist.keys():
    N.append(hist[p])
N.sort()   
#%%
for p in hist.keys():
    if hist[p]>N[-50] and len(p)>5:
        print(p,hist[p])
#%%
