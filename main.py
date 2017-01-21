#!/usr/bin/python3.5
#-*- coding: utf-8 -*-
'''
This is main file for sogang hackerton HanZoHap team
'''

import crawler
import gen_team_winrate as winrate
import HanZoHap

crawler.SummonerNameCrawler()

filenum=112
with open("names.txt", "r", encoding='utf-8') as F:
    f_lines = F.readlines()
    for line in f_lines:
        try:
            print(line)
            line = line.replace("\n", "")
            UserId = crawler.SummonerIdCrawler(line)
            #print(UserId)
            UserId = str(UserId)
            #print(type(UserId))

            List = crawler.MatchListCrawler(UserId)
            Match_List = set(List)
        except:
            pass
        #print(Match_List)
        try:
            filenum=crawler.MatchInfoCrawler(Match_List,filenum)
        except:
            print("pass")
            pass

#winrate.genTeamWinningRate(51)


