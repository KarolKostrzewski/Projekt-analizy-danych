from nba_api.stats.static import players

# Pobranie listy aktywnych graczy
player_list = players.get_active_players()

# Tworzenie listy aktywnych graczy po full_name isłownika z full_name i id gdzie kluczem jest full_name
active_players_full_name = []
active_players_id = dict()
for i in range(len(player_list)):
    full_name = player_list[i]['full_name']
    id = player_list[i]['id']
    active_players_full_name.append(full_name)
    active_players_id[full_name]=id

# Wybieranie przez użytkownika graczy, których chce porównać i liczbę sezonów wstecz do analizy
player1 = 'LeBron James' #input(f"Wybierz gracza nr1: ")
player2 = 'Jimmy Butler' #input(f"Wybierz gracza nr2: ")
player3 = 'Trae Young' #input(f"Wybierz gracza nr3: ")
seasons_countback = 7 #int(input(f"Wybierz ilość sezonów wstecz do analizy danych: "))
choosen_stat = 'FG_PCT' #input(f"Wybierz statystykę: ")
# Lista sezonów od 2000 do 2023 na sztywno
seasons=[
            '2000-01',
            '2001-02',
            '2002-03',
            '2003-04',
            '2004-05',
            '2005-06',
            '2006-07',
            '2007-08',
            '2008-09',
            '2009-10',
            '2010-11',
            '2011-12',
            '2012-13',
            '2013-14',
            '2014-15',
            '2015-16',
            '2016-17',
            '2017-18',
            '2018-19',
            '2019-20',
            '2020-21',
            '2021-22',
            '2022-23'
        ]
list_of_stats = [
                    'GP', 
                    'GS', 
                    'MIN', 
                    'FGM', 
                    'FGA', 
                    'FG_PCT', 
                    'FG3M', 
                    'FG3A', 
                    'FG3_PCT', 
                    'FTM', 
                    'FTA', 
                    'FT_PCT', 
                    'OREB', 
                    'DREB', 
                    'REB', 
                    'AST', 
                    'STL', 
                    'BLK', 
                    'TOV', 
                    'PF', 
                    'PTS'
                ]
# Statystyki z sezonów regularnych do wyboru i ich pozycja w liście ze słownika ze wszystkimi danymi 
stats= {
            "GP":6,
            "GS":7,
            "MIN":8,
            "FGM":9,
            "FGA":10,
            "FG_PCT":11,
            "FG3M":12,
            "FG3A":13,
            "FG3_PCT":14,
            "FTM":15,
            "FTA":16,
            "FT_PCT":17,
            "OREB":18,
            "DREB":19,
            "REB":20,
            "AST":21,
            "STL":22,
            "BLK":23,
            "TOV":24,
            "PF":25,
            "PTS":26,
        }
# Statystyki z podsumowania całej kariery
careers_stats = {
                    "PLAYER_ID":0,
                    "LEAGUE_ID":1,
                    "Team_ID":2,
                    "GP":3,
                    "GS":4,
                    "MIN":5,
                    "FGM":6,
                    "FGA":7,
                    "FG_PCT":8,
                    "FG3M":9,
                    "FG3A":10,
                    "FG3_PCT":11,
                    "FTM":12,
                    "FTA":13,
                    "FT_PCT":14,
                    "OREB":15,
                    "DREB":16,
                    "REB":17,
                    "AST":18,
                    "STL":19,
                    "BLK":20,
                    "TOV":21,
                    "PF":22,
                    "PTS":23
                }