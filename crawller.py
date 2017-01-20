import json
from bs4 import BeautifulSoup
import urllib.request

count=0

f=open('champNameById.txt','r')

for i in range(1,500):

    URL='https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/'+str(i)+'?api_key=RGAPI-a78e53a2-79a2-4191-8f80-80fd184fb059'

    try:
        x=urllib.request.urlopen(URL)
        rawData=x.read()
        encoding=x.info().get_content_charset('utf8')
        data=json.loads(rawData.decode(encoding))

        f.write(data)
        count+=1
    except:
        print("skip")

f.write(data)
f.close()

#with open('https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/1?api_key=RGAPI-a78e53a2-79a2-4191-8f80-80fd184fb059',encoding='utf-8') as jsonData:
#    champList=json.load(jsonData)

#print(champList)

#out=open('champNameById.txt','w')

#for i in champList:

#    print (i["id"],i["name"],file=out)

#out.close()
#