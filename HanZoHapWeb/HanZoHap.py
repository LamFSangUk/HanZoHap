#!/usr/bin/python3
# -*- coding: utf-8 -*-

from operator import itemgetter

def win_rate(name):
    champion_comb = {}
    with open("sample.bin", "rb") as Hap:
        bytebuffer = bytearray(Hap.read()).decode()
        byte_list = bytebuffer.split("\n")
        for line in byte_list:
            try:
                champ_line = line.split("|")
                rate = round(float(champ_line[-1]),2)
            except:
                pass
            try:
                for i in range(32):
                    on = list()
                    no = list()
                    for j in range(5):
                        if ((i & (1 << j)) > 0) == True:
                            on.append(champ_line[j])
                        else:
                            no.append(champ_line[j])
                    first = ' '.join(on)
                    second = ' '.join(no)
                    tp1 = (second, rate)
                    tp2 = (first, rate)
                    
                    if first not in champion_comb:
                        champion_comb[first] = list()
                    if second not in champion_comb:
                        champion_comb[second] = list()

                    champion_comb[first].append(tp1)
                    champion_comb[second].append(tp2)
            except:
                pass
    champion = set(champion_comb[name])
    result = sorted(champion, key=itemgetter(1), reverse = True) 
    try:
        return result[0:3]
    except:
        return result
