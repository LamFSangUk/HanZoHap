import json
import requests

getJSON = lambda response : response.json()

SummonerIdURL = lambda region, name, key : "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.4/summoner/by-name/" + name + "?api_key=" + key

CurrentGameURL = lambda region, SumID, key : "https://" + region + ".api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/"+ region + "/" + SumID + "?api_key=" + key



getJSONData = lambda URL  : getJSON(requests.get(URL))

refineName = lambda name : (name.lower()).replace(" ", "")

getSummonerID = lambda region, name, key : getJSONData(SummonerIdURL(region, name, key))[refineName]["id"]

getCurrentGame = lambda region, name, key : getJSONData(CurrentGameURL(region, str(getSummonerID(region, name, key)), key))

getParticipants = lambda region, name, key : getCurrentGame(region, name, key)["participants"]

getTeamId = lambda name, participants :  participants[0]["teamId"] if  participants[0]["summonerName"] == name else getTeamId(name, participants[1:])


def getSameTeam(region, name, key) :
   try:
      participants = getParticipants(region, name, key)
      teamId = getTeamId(name, participants)
      return list(map(lambda element : (element["summonerName"], element["championId"]), list(filter(lambda element : element["teamId"] == teamId and element["summonerName"] != name , participants))))
   except:
      return []
	  
   # getSameTeam("kr", "Nagne123", "RGAPI-9d1b6e21-7e34-4c01-9b20-a26041518479") yields,
   # ['Nagne123', 'Kf beyo', '내가강만식', '코잇컴짱좋네', '셔적적셔']
   
   # exceptions, errors result in empty list
      
#--------------------------------------------------------------------------------------------------	
	  
summonerStatsURL = lambda region, SumID, season, key : "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.3/stats/by-summoner/" + SumID + "/ranked?season=SEASON" + season + "&api_key=" + key
	  
getSummonerStats = lambda region, name, season, key :   getJSONData(summonerStatsURL(region, str(getSummonerID(region, name, key)), season, key))

computeStatsFromJSON = lambda 

getChampData = lambda 

getTeammateStats = lambda region, name, season, key : 
   
   
   

