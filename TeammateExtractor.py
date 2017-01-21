import json
import requests

getJSON = lambda response : response.json()

SummonerIdURL = lambda requestData : "https://" + requestData[0] + ".api.pvp.net/api/lol/" + requestData[0] + "/v1.4/summoner/by-name/" + requestData[1] + "?api_key=" + requestData[2]

CurrentGameURL = lambda region, SumID, key : "https://" + region + ".api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/"+ region + "/" + SumID + "?api_key=" + key

requestJSON = lambda URL  : getJSON(requests.get(URL))

refineName = lambda name : (name.lower()).replace(" ", "")

getSummonerID = lambda requestData : requestJSON(SummonerIdURL(requestData))[refineName(requestData[1])]["id"]

getCurrentGame = lambda requestData : requestJSON(CurrentGameURL(requestData[0], str(getSummonerID(requestData)), requestData[2]))

getParticipants = lambda requestData : getCurrentGame(requestData)["participants"]

getTeamId = lambda name, participants :  participants[0]["teamId"] if  participants[0]["summonerName"] == name else getTeamId(name, participants[1:])


def getSameTeam(requestData) :
   try:
      participants = getParticipants(requestData)
      teamId = getTeamId(requestData[1], participants)
      return list(map(lambda element : (element["summonerName"], element["championId"]), list(filter(lambda element : element["teamId"] == teamId and element["summonerName"] != requestData[1] , participants))))
   except:
      return []


   ### requestData is a tuple of (region, SummonerName, API Key)!! All strings!!
   # getSameTeam("kr", "Nagne123", "RGAPI-9d1b6e21-7e34-4c01-9b20-a26041518479") yields,
   # ['Nagne123', 'Kf beyo', '내가강만식', '코잇컴짱좋네', '셔적적셔']
   
   # exceptions, errors result in empty list
      
   #--------------------------------------------------------------------------------------------------	
	  
summonerStatsURL = lambda region, SumID, season, key : "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.3/stats/by-summoner/" + SumID + "/ranked?season=SEASON" + season + "&api_key=" + key
	  
getSummonerStats = lambda region, name, season, key :   getJSONData(summonerStatsURL(region, str(getSummonerID(region, name, key)), season, key))

computeStatsFromJSON = lambda 

getChampData = lambda 

getTeammateStats = lambda region, name, season, key : 
   
   
   

