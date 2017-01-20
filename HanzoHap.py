#!/usr/bin/python3
#-*- coding: utf-8 -*-
from operator import itemgetter

champ_ID = {}

for i in range(0, 150):
    champ_ID[i] = list()

with open("test.bin", "rb") as Hap:
    byteBuffer = bytearray(Hap.read()).decode()
    byte_list = byteBuffer.split("\n")
    for line in byte_list:
        try:
            champ_line = line.split("|")
            for champ in champ_line[0:4]:
                Id = int(champ)
                tp = (champ_line, champ_line[-1])
                champ_ID[Id].append(tp)
        except: 
            pass

name = int(input())
print(sorted(champ_ID[name],key=itemgetter(1)))

