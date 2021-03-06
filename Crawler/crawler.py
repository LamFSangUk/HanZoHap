#-*- coding: utf-8 -*-

import json
import urllib.request
import bs4
import requests
from API import api_key

api_idx=20
api_used=0

def ChampionCrawler():

    count=0

    f=open('champNameById.txt','w')

    for i in range(1,500):

        URL='https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/'+str(i)+'?api_key='\
            +api_key[2]

        try:
            x=urllib.request.urlopen(URL)
            rawData=x.read()
            encoding=x.info().get_content_charset('utf-8')
            data=json.loads(rawData.decode(encoding))
            f.write(str(data['id'])+' '+str(data['name'])+'\n')
            #strdata=data['id']+' '+data['name']
            #print(strdata)
            #f.write()
            count+=1
        except:
            print("skip")

    f.write(str(count))
    f.close()

def SummonerNameCrawler():

    with open('names.txt', 'w', encoding='utf-8') as fw:
        from_index = int(input('From : '))
        to_index = int(input('To : '))
        num_of_names = to_index - from_index + 1
        num_pages = num_of_names // 50 + 2
        cur_page = from_index // 50 + 1
        start_count = (cur_page - 1) * 50 + 1
        count = 0

        url = 'http://lol.inven.co.kr/dataninfo/ladder/index.php?pg=' + str(cur_page)
        html = urllib.request.urlopen(url)
        soup = bs4.BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            if link.get('href') is not None \
                    and link.get('href')[:48] == "http://lol.inven.co.kr/dataninfo/player/list.php":
                if start_count >= from_index:
                    if len(link.contents) != 0:
                        print(' '.join(link.contents[0].split()), file=fw)
                    count += 1
                else:
                    start_count += 1

                if count == num_of_names:
                    break

        cur_page += 1

        while count != num_of_names:
            url = 'http://lol.inven.co.kr/dataninfo/ladder/index.php?pg=' + str(cur_page)
            html = urllib.request.urlopen(url)
            soup = bs4.BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a'):
                if link.get('href') is not None \
                        and link.get('href')[:48] == "http://lol.inven.co.kr/dataninfo/player/list.php":
                    if len(link.contents) != 0:
                        print(' '.join(link.contents[0].split()), file=fw)
                    count += 1
                    if count == num_of_names:
                        break

            cur_page += 1


def SummonerIdCrawler(summonerName):
    #summonerName = summonerName.replace(" ", "%20")
    #print(usummonerName).encode('utf-8')
    #global api_idx
    #global api_used

    #if api_used>=300 :
    #    api_idx+=2
    #    api_used=0
    #    if api_idx>=len(api_key) : api_idx=0

    #summonerName=u = unicode(summonerName, "UTF-8")
    URL=u'https://kr.api.pvp.net/api/lol/kr/v1.4/summoner/by-name/%s?api_key=%s'%(summonerName,api_key[2])
    #api_used+=1

    # print("URL " + URL)
    try:
        getJSON = lambda response: response.json()

        data = lambda URL: getJSON(requests.get(URL))
        data=data(URL)

        #print(summonerName)
        summonerName=summonerName.replace(" ", "").lower()

        print(data[summonerName])
        return data[summonerName]['id']


    except:
        pass
        #return 'err'

def MatchListCrawler(summonerId):
    #global api_idx

#    count=0
    matchIdList=[]
    URL='https://kr.api.pvp.net/api/lol/kr/v2.2/matchlist/by-summoner/'+summonerId+'?api_key='\
        +api_key[2]
    print(summonerId)

    try:
        x = urllib.request.urlopen(URL)
        rawData = x.read()
        encoding = x.info().get_content_charset('utf-8')
        data = json.loads(rawData.decode(encoding))
        data=data['matches']
        for game in data:
            #if game['season']=='PRESEASON2017':
            #print(game['matchId'])
            matchIdList.append(game['matchId'])
            #count+=1
        #for matchInfo in data.values():
        #    print(matchInfo['matchId'])
        #print(count)
        return matchIdList
    except:
        pass

def MatchInfoCrawler(matchListSet,filenumstart):
    #global api_idx

    #idx=api_idx+1
    #used=0
    filenum=filenumstart
    #print(filenum)
    for matchInfo in matchListSet:
        try:
            #print(matchInfo)
            URL = 'https://kr.api.pvp.net/api/lol/kr/v2.2/match/' + str(matchInfo) + '?api_key=' \
                  + api_key[2]
            # used+=1
            # if used>=300 :
            #    idx+=1
            #    used=0
            #    if idx>=len(api_key):
            #        idx=0

            x = urllib.request.urlopen(URL)
            rawData = x.read()
            encoding = x.info().get_content_charset('utf-8')
            data = json.loads(rawData.decode(encoding))
            jsonString = json.dumps(data)
            # import pprint
            # pprint.pprint(jsonString)
            f = open('json_data/match' + str(filenum) + '.json', 'w')
            f.write(str(jsonString))
            print("here")
            f.close()
            filenum += 1
        except:
            pass
    return filenum
