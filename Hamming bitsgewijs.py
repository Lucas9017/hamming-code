# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 17:05:37 2022

@author: ravdk
"""
import random
def decimaalBinair(decimaal):
    if decimaal == 0:
        return 0
    else:
        binair = []
        while decimaal > 0:
            if decimaal % 2 == 0:
                binair.append(0)
                decimaal = decimaal // 2
            else:
                binair.append(1)
                decimaal = decimaal // 2
        
        tekst = ""
    for i in range(0,len(binair)): 
        tekst += str(binair[len(binair)-i-1])
    return tekst

def binairDecimaal(binair):
    lijst = [int(x) for x in str(binair)]
    decimaal = 0
    for i in range(0,len(lijst)):
        decimaal += lijst[i] * 2**(len(lijst)-i-1)
    return decimaal
    
def nibbles(input):
    binair=''
    for i in input:
        x=decimaalBinair(ord(i))
        l=8-len(x)
        if l==0:
            binair+=x
        else:
            binair+='0'*l+x
    lengte=len(binair)
    lijst=[[] for i in range(0,lengte,4)]
    for i in range(len(lijst)):
        for j in range(0,4):
            lijst[i]+=[int(binair[i*4+j])]
    return lijst

def parity_vector(input):
    lijst=[]
    for i in range(len(input)):
        p1=input[i][0]^input[i][1]^input[i][3]
        p2=input[i][0]^input[i][2]^input[i][3]
        p3=input[i][1]^input[i][2]^input[i][3]
        lijst+=[[p1,p2,input[i][0],p3,input[i][1],input[i][2],input[i][3]]]
    return lijst

def check_correct(input):
    lijst=[]
    for i in range(len(input)):
        p1=input[i][0]^input[i][2]^input[i][4]^input[i][6]
        p2=input[i][1]^input[i][2]^input[i][5]^input[i][6]
        p3=input[i][3]^input[i][4]^input[i][5]^input[i][6]
        if p1==0 and p2==0 and p3==0:
            lijst+=[input[i]]
        else:
            plek=binairDecimaal(str(p3)+str(p2)+str(p1))-1
            input[i][plek]=input[i][plek]^1
            lijst+=[input[i]]
    return lijst

def decodeer(input):
    string=''
    uitvoer=''
    for i in range(len(input)):
        string+=str(input[i][2])+str(input[i][4])+str(input[i][5])+str(input[i][6])
    for i in range(0,len(string),8):
        uitvoer+=chr(binairDecimaal(string[i:i+8]))
    return uitvoer

def random_verandering(input,aantal):
    verstuur=input
    lijst=[]
    for i in range(len(verstuur)):
        lijst+=verstuur[i]
    lengte=len(lijst)
    k = random.sample(range(0,lengte),aantal)
    for j in k:
        lijst[j]=lijst[j]^1
    ontvangst=[]
    for i in range(0,lengte,7):
        ontvangst+=[list(lijst[i:i+7])]
    return ontvangst
        
def hamming(input,aantal):
    n=nibbles(input)
    v=parity_vector(n)
    r=random_verandering(v,aantal)
    print('Uw boodschap na de fouten is: ',decodeer(r))
    c=check_correct(r)
    d=decodeer(c)
    return d

def hamming_code():
    code=str(input('Wat wilt u versturen? '))
    binair=''
    for i in code:
        x=decimaalBinair(ord(i))
        l=8-len(x)
        if l==0:
            binair+=x
        else:
            binair+='0'*l+x
    lengte=len(binair)
    aantal=int(input('Uw boodschap bevat '+str(lengte )+' bits. Hoeveel fouten moeten er ontstaan in deze bits bij het versturen? '))
    return hamming(code,aantal)