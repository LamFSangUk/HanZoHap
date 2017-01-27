import requests
from functools import partial

getJSON = lambda response : response.json()

SummonerIdURL = lambda requestData : "https://" + requestData[0] + ".api.pvp.net/api/lol/" + requestData[0] + "/v1.4/summoner/by-name/" + requestData[1] + "?api_key=" + requestData[2]

CurrentGameURL = lambda region, SumID, key : "https://" + region + ".api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/"+ region + "/" + SumID + "?api_key=" + key

requestJSON = lambda URL  : getJSON(requests.get(URL))

refineName = lambda name : (name.lower()).replace(" ", "")

getSummonerID = lambda requestData : requestJSON(SummonerIdURL(requestData))[refineName(requestData[1])]["id"]

getCurrentGame = lambda requestData : requestJSON(CurrentGameURL(requestData[0], str(getSummonerID(requestData)), requestData[2]))

getParticipants = lambda requestData : getCurrentGame(requestData)["participants"]

getTeamId = lambda name, participants :  participants[0]["teamId"] if  participants[0]["summonerName"] == name else getTeamId(name, participants[1:])


def getSameTeam(requestData):
	try:
		participants = getParticipants(requestData)
		teamId = getTeamId(requestData[1], participants)
		return list(map(lambda element : (element["summonerName"], element["championId"]), list(filter(lambda element : element["teamId"] == teamId and element["summonerName"] != requestData[1] , participants))))
	except:
		return []

summonerStatsURL = lambda region, SumID, season, key : "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.3/stats/by-summoner/" + SumID + "/ranked?season=SEASON" + season + "&api_key=" + key

getSummonerStats = lambda requestData, season :   requestJSON(summonerStatsURL(requestData[0], str(getSummonerID(requestData)), season, requestData[2]))

getChampions = lambda data : data["champions"]

findChampion = lambda id, champs : champs[0] if champs[0]["id"] == id else findChampion(id, champs[1:])

getStatsByChamp = lambda id, data : findChampion(id, getChampions(data))["stats"]

getSummonerChampStats = lambda requestData, season, id  : getStatsByChamp(id, getSummonerStats(requestData, season))

def computeWinStats(stats):
	lost = stats["totalSessionsLost"]
	won = stats["totalSessionsWon"]
	total = lost + won
	return (round(won/total * 100, 2), total)
   
   
def makeTuple(requestData, season, elem):
	try:
		result = computeWinStats(getSummonerChampStats((requestData[0], elem[0], requestData[2]), season, elem[1]))
	except:
		result = (0,0)
	return (elem[0], result)

   
getTeammateWinStats = lambda requestData, season : list(map(partial(makeTuple, requestData, season,), getSameTeam(requestData)))




#---------------------------------------------------------------------------------------------------------------
#           This module calculates the Win/Lose ration of you current teammates on their current champions
#           Using the 'getTeammateWinStats' function will return a list of tuples containing the data
#
####   SYNTAX: getTeammateWinStats((region, UserName, API-Key), Season)                           
####   yields, [('Summoner', (win/lose, total)), ('Summoner', (win/lose, total)), ('Summoner', (win/lose, total)), ('Summoner', (win/lose, total))]
####   exceptions result in ('UserName', (0,0)) which is mostly because the summoner has never picked that champion during this season



# example:




# result: [('Fq Gaia', (100.0, 2)), ('신들린써페', (84.0, 68)), ('원딜프로지망1', (70.0, 107)), ('Life one', (67.0, 36))]
	
import json
from flask import (
	Flask, 
	render_template,
	request,
)

champdict={}
champion=[]

app = Flask(__name__)
@app.route('/')
def home():
	f = open("champNameById.txt",'r')
	line = f.readlines()
	for champ in line:
		champion.append(' '.join(champ.split()[1:]))
		champdict[' '.join(champ.split()[1:])]=champ.split()[0]
	f.close()
	return render_template('HZHmain.html', champion=champion)    
@app.route('/api/datas/', methods=['GET','POST'])
def my_form_post():
	if request.method=='POST':
		selectlist=[]
		finallist=[]
		SummonerName = request.form['SummonerName']
		champ1 = request.form.get('champ1')	
		if champ1!="default":
			selectlist.append(int(champdict[champ1]))
		champ2 = request.form.get('champ2')
		if champ2!="default":
			selectlist.append(int(champdict[champ2]))
		champ3 = request.form.get('champ3')
		if champ3!="default":
			selectlist.append(int(champdict[champ3]))
		champ4 = request.form.get('champ4')
		if champ4!="default":
			selectlist.append(int(champdict[champ4]))
		champ5 = request.form.get('champ5')
		if champ5!="default":
			selectlist.append(int(champdict[champ5]))
		try:
			selectlist.sort()
			selectlist=[str(x) for x in selectlist]
			print(' '.join(selectlist))
			import HanZoHap
			winninglist=HanZoHap.win_rate(' '.join(selectlist))
			finallist=selectlist+winninglist[0][0].split()
			winrate=winninglist[0][1]
			print(winrate)
			finallist=[int(x) for x in finallist]
			finallist.sort()
			finallist=[str(x) for x in finallist]
			requestData = ("kr", SummonerName, "RGAPI-9d1b6e21-7e34-4c01-9b20-a26041518479")
			print(getTeammateWinStats(requestData, "2017"))
		except:
			print("Exception?")
			pass
		return render_template('HZHresult.html',picklist=finallist,winrate=winrate,champion=champion)

#@app.route('HZHmain.html')
#def my_link():
#
#  return 'Click.'

if __name__ == '__main__':
	app.run(debug=True)
