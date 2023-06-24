import requests
import json



url = "https://api.snooker.org/?t=10&st=p&s=2022"
api_key = "KarolProject"
headers = {"X-Requested-By": api_key}
response = requests.get(url, headers=headers)
data = response.json()

def save_json_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Zapis danych JSON do pliku
save_json_to_file(data, "snooker_players_2022.json")

