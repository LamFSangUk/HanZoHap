import json

def genTeamWinningRate(file_num):
    #file_num = int(input('How many files are there? : '))

    with open('result.txt', 'w') as fw:
        for i in range(1, file_num + 1):

            file_name = 'json_data/match' + str(i) + '.json'

            with open(file_name, encoding='utf-8') as json_data:
                json_dict = json.load(json_data)

                win_rate = {}

                team1_champ_list = []
                team2_champ_list = []

                # which team won a game?
                first_participant = json_dict["participants"][0]
                if first_participant['teamId'] == 100:
                    if first_participant['stats']['winner'] == True:
                        which_team_win = 1
                    else:
                        which_team_win = 2
                else:
                    if first_participant['stats']['winner'] == True:
                        which_team_win = 2
                    else:
                        which_team_win = 1

                # make a champ list
                for participant in json_dict["participants"]:
                    # assume that teamId is 100 or 200
                    if participant['teamId'] == 100:
                        team1_champ_list.append(participant["championId"])
                    elif participant['teamId'] == 200:
                        team2_champ_list.append(participant["championId"])

                team1_champ_list = tuple(sorted(team1_champ_list))
                team2_champ_list = tuple(sorted(team2_champ_list))

                if team1_champ_list not in win_rate:
                    if which_team_win == 1:
                        win_rate[team1_champ_list] = {'totalGameNum': 1, 'win': 1}
                    else:
                        win_rate[team1_champ_list] = {'totalGameNum': 1, 'win': 0}
                else:
                    win_rate[team1_champ_list]['totalGameNum'] += 1
                    if which_team_win == 1:
                        win_rate[team1_champ_list]['win'] += 1

                if team2_champ_list not in win_rate:
                    if which_team_win == 2:
                        win_rate[team2_champ_list] = {'totalGameNum': 1, 'win': 1}
                    else:
                        win_rate[team2_champ_list] = {'totalGameNum': 1, 'win': 0}
                else:
                    win_rate[team2_champ_list]['totalGameNum'] += 1
                    if which_team_win == 2:
                        win_rate[team2_champ_list]['win'] += 1

            for team_comb, win_lose in win_rate.items():
                print(str(team_comb) + ' ' + str(win_lose), file=fw)
