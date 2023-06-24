import json
import requests

# def get_snooker_data():
#     url = "https://api.snooker.org/?t=10&st=p&s=2022"
#     headers = {"X-requested-by": "KarolProject"}
#     response = requests.get(url, headers=headers)
#     data = response.json()
#     return data

# snooker_data = get_snooker_data()

# active_pro_players_2022 = dict()
# for i in snooker_data:
#     active_pro_players_2022[i["FirstName"]+" "+ i["LastName"]] = i["ID"]

# print(active_pro_players_2022)

# def save_dict_to_file(dictionary, filename):
#     with open(filename, 'w') as file:
#         json.dump(dictionary, file, indent=4)

# Zapis słownika do pliku
# save_dict_to_file(active_pro_players_2022, "pro_players.json")
# {'ID': 7267231, 
#  'EventID': 1315, 
#  'Round': 19, 
#  'Number': 1, 
#  'Player1ID': 1, 
#  'Score1': 3, 
# 'Walkover1': False, 
# 'Player2ID': 50, 
# 'Score2': 1, 
# 'Walkover2': False, 
# 'WinnerID': 1, 
# 'Unfinished': False, 'OnBreak': False, 'Status': 3, 'WorldSnookerID': 855174, 'LiveUrl': '', 
# 'DetailsUrl': '', 'PointsDropped': False, 'ShowCommonNote': True, 'Estimated': False, 'Type': 1, 'TableNo': 0, 'VideoURL': '', 'InitDate': '2022-06-08T07:36:05Z', 'ModDate': '2022-07-11T11:26:24Z', 'StartDate': '2022-07-11T11:26:24Z', 'EndDate': '2022-07-11T12:36:22Z', 'ScheduledDate': '2022-07-11T11:00:00Z', 'FrameScores': '', 'Sessions': '', 'Note': '', 'ExtendedNote': ''}

def get_snooker_data(player_id):
    url = f"https://api.snooker.org/?t=8&p={player_id}&s=2022"
    headers = {"X-requested-by": "KarolProject"}
    response = requests.get(url, headers=headers)
    data = response.json() 
    return data


x = get_snooker_data(1)
print(x[1]['WinnerID'])
y=0

for i in x:
    if i['WinnerID'] == 1:
        y+=1

print(y,len(x))