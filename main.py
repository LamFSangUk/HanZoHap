#!/usr/bin/python3.5
#-*- coding: utf-8 -*-
'''
This is main file for sogang hackerton HanZoHap team
'''

import crawler
import gen_team_winrate as winrate
import HanZoHap

crawler.SummonerNameCrawler()
with open("names.txt", "r", encoding='utf-8') as F:
    f_lines = F.readlines()
    for line in f_lines:
        print(line)
        line = line.replace("\n", "")
        UserId = crawler.SummonerIdCrawler(line)
        UserId = str(UserId)
        print(type(UserId))
        Match_List = set()
        List = crawler.MatchListCrawler(UserId)
        Match_List.union(List)
    print(Match_List)
    filenum = crawler.MatchInfoCrawler(Match_List)
    winrate.genTeamWinningRate(int(filenum))


