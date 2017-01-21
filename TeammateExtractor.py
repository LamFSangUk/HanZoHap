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
   return (round((won / lost), 2) * 100, total)
   
   
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

def main():
   requestData = ("kr", "BoRoona", "RGAPI-9d1b6e21-7e34-4c01-9b20-a26041518479")
   print(getTeammateWinStats(requestData, "2017"))


# result: [('Fq Gaia', (100.0, 2)), ('신들린써페', (84.0, 68)), ('원딜프로지망1', (70.0, 107)), ('Life one', (67.0, 36))]
	
	
if __name__ == '__main__':
    main()

