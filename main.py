#!/usr/bin/python3.5
#-*- coding: utf-8 -*-
'''
This is main file for sogang hackerton HanZoHap team
'''

import crawler
from HanZoHap import win_late

crawler.SummonerNameCrawler()
with open("names.txt", "r", encoding='utf-8') as F:
    f_lines = F.readlines()
    print(lines)
    for line in f_lines:
        print(line)
        UserId = crawler.SummonerIdCrawler(line)
        Match_List = set()
        Match_List.union(crawler.MatchListCrawler(UserId))
        crawler.MatchInfoCrawler(Match_List)
        

