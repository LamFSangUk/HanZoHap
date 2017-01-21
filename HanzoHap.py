#!/usr/bin/python3
# -*- coding: utf-8 -*-

from operator import itemgetter

def win_late(name):
    champ_ID = {}
    champ_comb = {}
    
    with open("HanzoHap.bin", "rb") as Hap:
        bytebuffer = bytearray(Hap.read()).decode()
        byte_list = bytebuffer.split("\n")
        for line in byte_list:
            try:
                champ_line = line.split("|")
            except:
                pass
            champ_word = ""
    
            for sword in champ_line[0:5]:
                champ_word += sword + " "
    
            for champ in champ_line[0:5]:
                word = champ_word.replace(champ, "")
                word = word.replace("  ", " ")
                word = word.strip()
                    
                Id = int(champ)
                if Id not in champ_ID:
                    champ_ID[Id] = list()
                
                if word not in champ_comb:
                    champ_comb[word] = list()
                
                tp = (word, champ_line[-1])
                champ_ID[Id].append(tp)
                tp = (champ, champ_line[-1])
                champ_comb[word].append(tp)
   
    
    result = sorted(champ_ID[name], key=itemgetter(1))
    
    try:
        print(result[0:5])
    except:
        print(result)
