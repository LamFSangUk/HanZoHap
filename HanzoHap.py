#!/usr/bin/python3
# -*- coding: utf-8 -*-

from operator import itemgetter


def win_rate(name):
    champ_ID = {}
    champ_comb = {}
    with open("test.bin", "rb") as Hap:
        bytebuffer = bytearray(Hap.read()).decode()
        byte_list = bytebuffer.split("\n")
        for line in byte_list:
            try:
                champ_line = line.split("|")
            except:
                pass
            for champ in champ_line[0:5]:
                champion = champ_line[0:5]
                champion.remove(champ)
                champ_tmp = champion
                champ_str = '|'.join(champion)
                try:
                    Id = int(champ)
                    rate = float(champ_line[-1])
                except:
                    pass
                if Id not in champ_ID:
                    champ_ID[Id] = list()

                if champ_str not in champ_comb:
                    champ_comb[champ_str] = list()
                tp = (champ_tmp, rate)
                champ_ID[Id].append(tp)
                tp = (champ, rate)
                champ_comb[champ_str].append(tp)
    result = sorted(champ_ID[name], key=itemgetter(1))
    print(result)

    try:
        print(result[0:5])
    except:
        print(result)