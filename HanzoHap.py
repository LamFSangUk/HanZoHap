#!/usr/bin/python3
#-*- coding: utf-8 -*-

from operator import itemgetter
champ_ID = {}
champ_comb = {}

with open("test.bin", "rb") as Hap:
    byteBuffer = bytearray(Hap.read()).decode()
    byte_list = byteBuffer.split("\n")
    for line in byte_list:
        try:
            champ_line = line.split("|")
            
            champ_word = ""

            for sword in champ_line[0:5]:
                champ_word += sword + " "

            for champ in champ_line[0:5]:
                
                word = champ_word.replace(champ,"")
                word = word.replace("  ", " ")
                word = word.strip()

                ID = int(champ)
                tp = (word, champ_line[-1])
                if ID not in champ_ID:
                    champ_ID[ID] = []
                champ_ID[ID].append(tp)  
                
                if word not in  champ_comb:
                    champ_comb[word] = []
    
                tp =  (champ, champ_line[-1])
                champ_comb[word].append(tp)
        except: 
            pass

print(champ_comb)

name = int(input())
result = sorted(champ_ID[name], key = itemgetter(1))
try:
    print(result[0:5])
except:
    print(result)
