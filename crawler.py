import json
import urllib.request

def ChampionCrawler():

    count=0

    f=open('champNameById.txt','w')

    for i in range(1,500):

        URL='https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/'+str(i)+'?api_key=RGAPI-a78e53a2-79a2-4191-8f80-80fd184fb059'

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

def SummonerCrawler():

    numSummoners=int(input())
    print(numSummoners)

    for i in range(numSummoners):
        summonerName=input()
        URL='https://kr.api.pvp.net/api/lol/kr/v1.4/summoner/by-name/'+summonerName+'?api_key=RGAPI-a78e53a2-79a2-4191-8f80-80fd184fb059'

        try:
            x = urllib.request.urlopen(URL)
            rawData = x.read()
            encoding = x.info().get_content_charset('utf-8')
            data = json.loads(rawData.decode(encoding))
            for suInfo in data.values():
                print(suInfo['name'],suInfo['id'])

        except:
            pass

def MatchlistCrawler():

    count=0
    summonerID=input()

    URL='https://kr.api.pvp.net/api/lol/kr/v2.2/matchlist/by-summoner/'+summonerID+'?api_key=RGAPI-a78e53a2-79a2-4191-8f80-80fd184fb059'

    try:
        x = urllib.request.urlopen(URL)
        rawData = x.read()
        encoding = x.info().get_content_charset('utf-8')
        data = json.loads(rawData.decode(encoding))
        data=data['matches']
        for game in data:
           if game['season']=='PRESEASON2017':
            print(game['matchId'])
            count+=1
        #for matchInfo in data.values():
        #    print(matchInfo['matchId'])
        print(count)
    except:
        pass

def MatchInfoCrawler():

    matchInfo=input()

    URL='https://kr.api.pvp.net/api/lol/kr/v2.2/match/'+matchInfo+'?api_key=RGAPI-a78e53a2-79a2-4191-8f80-80fd184fb059'
    x = urllib.request.urlopen(URL)
    rawData = x.read()
    encoding = x.info().get_content_charset('utf-8')
    data = json.loads(rawData.decode(encoding))
    jsonString=json.dumps(data)
    import pprint
    pprint.pprint(jsonString)
    f=open('match1.json','w')
    f.write(jsonString)
    f.close()

print("start")
MatchInfoCrawler()