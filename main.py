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
        UserId = crawler.SummonerIdCrawler(line)
        Match_List = set()
        Match_List.union(crawler.MatchListCrawler(UserId))
        filenum = crawler.MatchInfoCrawler(Match_List)
        winrate.genTeamWinningRate(filenum)


