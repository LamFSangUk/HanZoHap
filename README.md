# HanZoHap
prototype for automatic champion recommendation for LOL

Using Riot API, We got the Match Data to calculate the winning rate of combination of champions.
We crawled it, and produce the champion combinations' winrate.
We saved it by JSON data file.

For Web, the user can input the champion's names from one to five. Then, the server find the champion combination that has the best winrate.
After find it, the user can get the information of best winrate's champiton combination.
Then just play for that combination! You must win!
