#!/usr/bin/python3
# -*- coding: utf-8 -*-

from operator import itemgetter


def win_rate(name):
    champion_comb = {}
    with open("test.bin", "rb") as Hap:
        bytebuffer = bytearray(Hap.read()).decode()
        byte_list = bytebuffer.split("\n")
        for line in byte_list:
            try:
                champ_line = line.split("|")
                rate = float(champ_line[-1])
                print(rate)
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
                    first = '|'.join(on)
                    second = '|'.join(no)
                    tp1 = (second, rate)

                    tp2 = (first, rate)
                    print(tp1, tp2)
                    champion_comb[first] = tp1
                    champion_comb[second] = tp2
            except:
                pass
    print(champion_comb)
'''
    result = sorted(champ_ID[name], key=itemgetter(1))
    print(result)

    try:
        print(result[0:5])
    except:
        print(result)
'''
