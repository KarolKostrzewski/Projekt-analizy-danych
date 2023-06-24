from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players

# Tworzenie metody do wygenerowania list i słowników aktywnych graczy
def pobierz_graczy():
    # Pobranie listy aktywnych graczy
    player_list = players.get_active_players()
    # Tworzenie listy aktywnych graczy po full_name isłownika z full_name i id gdzie kluczem jest full_name
    active_players_full_name = []
    active_players_id = dict()
    seasons_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    list_stats = [
                "Mecze zagrane",
                "Mecze jako pierwsza 5",
                "Minuty",
                "Rzuty trafione",
                "Rzuty oddane",
                "Skuteczność rzutów",
                "Rzuty za 3 trafione",
                "Rzuty za 3 oddane",
                "Skuteczność rzutów za 3",
                "Rzuty z fauli trafione",
                "Rzuty z fauli oddane",
                "Skuteczność rzutów z fauli",
                "Zbiórki w ataku",
                "Zborki w defensywie",
                "Zbiórki",
                "Asysty",
                "Kradzieże",
                "Bloki",
                "Straty",
                "Faule osobiste",
                "Punkty",
                ]
    for i in range(len(player_list)):
        full_name = player_list[i]['full_name']
        id = player_list[i]['id']
        active_players_full_name.append(full_name)
        active_players_id[full_name]=id
    return active_players_full_name,active_players_id,seasons_list,list_stats

# Tworzenie klasy, która zbiera dane, przetwarza i rysuje wykres
class Nba():

    def __init__(self,player1,player2,player3,seasons_countback,choosen_stat,active_players_id):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.seasons_countback = int(seasons_countback)
        self.choosen_stat = choosen_stat
        self.active_players_id = active_players_id
        self.active_players_full_name = self.active_players_id.keys()
        self.seasons=[
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
        self.stats= {
                    "Mecze zagrane":6,
                    "Mecze jako pierwsza 5":7,
                    "Minuty":8,
                    "Rzuty trafione":9,
                    "Rzuty oddane":10,
                    "Skuteczność rzutów":11,
                    "Rzuty za 3 trafione":12,
                    "Rzuty za 3 oddane":13,
                    "Skuteczność rzutów za 3":14,
                    "Rzuty z fauli trafione":15,
                    "Rzuty z fauli oddane":16,
                    "Skuteczność rzutów z fauli":17,
                    "Zbiórki w ataku":18,
                    "Zborki w defensywie":19,
                    "Zbiórki":20,
                    "Asysty":21,
                    "Kradzieże":22,
                    "Bloki":23,
                    "Straty":24,
                    "Faule osobiste":25,
                    "Punkty":26,
                }
        self.choosen_stat_idx = self.stats[self.choosen_stat]

    def pobierz_dane(self):

        # Pobieranie id gracza, którego użytkownik wybrał
        self.id1 = self.active_players_id[self.player1]
        self.id2 = self.active_players_id[self.player2]
        self.id3 = self.active_players_id[self.player3]

        # Pobieranie danych wybranych graczy
        self.career1 = playercareerstats.PlayerCareerStats(player_id=self.id1) 
        self.career2 = playercareerstats.PlayerCareerStats(player_id=self.id2) 
        self.career3 = playercareerstats.PlayerCareerStats(player_id=self.id3) 

        # Tworzenie słownika
        self.nba1=self.career1.get_dict()
        self.nba2=self.career2.get_dict()
        self.nba3=self.career3.get_dict()

        # Tworzenie list z danymi z ostatnich n sezonów (jeśli gracz nie był w tym czasie w lidze, to uzupełniamy listę Nullem)
        self.stat1 = []
        if len(self.nba1["resultSets"][0]["rowSet"]) >= self.seasons_countback:
            for i in range(len(self.nba1["resultSets"][0]["rowSet"])-self.seasons_countback,len(self.nba1["resultSets"][0]["rowSet"])):
                self.stat1.append(self.nba1["resultSets"][0]["rowSet"][i][self.choosen_stat_idx])
        else:
            for i in range(len(self.nba1["resultSets"][0]["rowSet"])):
                self.stat1.append(self.nba1["resultSets"][0]["rowSet"][i][self.choosen_stat_idx])
            for i in range(self.seasons_countback- len(self.nba1["resultSets"][0]["rowSet"])):
                self.stat1.insert(0,None)
        self.stat2 = []
        if len(self.nba2["resultSets"][0]["rowSet"]) >= self.seasons_countback:
            for i in range(len(self.nba2["resultSets"][0]["rowSet"])-self.seasons_countback,len(self.nba2["resultSets"][0]["rowSet"])):
                self.stat2.append(self.nba2["resultSets"][0]["rowSet"][i][self.choosen_stat_idx])
        else:
            for i in range(len(self.nba2["resultSets"][0]["rowSet"])):
                self.stat2.append(self.nba2["resultSets"][0]["rowSet"][i][self.choosen_stat_idx])
            for i in range(self.seasons_countback- len(self.nba2["resultSets"][0]["rowSet"])):
                self.stat2.insert(0,None)
        self.stat3 = []
        if len(self.nba3["resultSets"][0]["rowSet"]) >= self.seasons_countback:
            for i in range(len(self.nba3["resultSets"][0]["rowSet"])-self.seasons_countback,len(self.nba3["resultSets"][0]["rowSet"])):
                self.stat3.append(self.nba3["resultSets"][0]["rowSet"][i][self.choosen_stat_idx])
        else:
            for i in range(len(self.nba3["resultSets"][0]["rowSet"])):
                self.stat3.append(self.nba3["resultSets"][0]["rowSet"][i][self.choosen_stat_idx])
            for i in range(self.seasons_countback- len(self.nba3["resultSets"][0]["rowSet"])):
                self.stat3.insert(0,None)
        # Tworzenie listy n sezonów
        self.selected_seasons = []
        self.frame1 = self.career1.get_data_frames()[1]
        self.frame2 = self.career2.get_data_frames()[1]
        self.frame3 = self.career3.get_data_frames()[1]
        for i in range(self.seasons_countback,0,-1):
            self.selected_seasons.append(self.seasons[len(self.seasons)-i])        
        return self.stat1,self.stat2,self.stat3,self.active_players_full_name,self.active_players_id,self.id1,self.id2,self.id3,self.selected_seasons,self.frame1,self.frame2,self.frame3   
    
class PostSeason():

    def __init__(self,player1,player2,player3,seasons_countback,choosen_stat,active_players_id):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.seasons_countback = int(seasons_countback)
        self.choosen_stat = choosen_stat
        self.active_players_id = active_players_id
        self.active_players_full_name = self.active_players_id.keys()
        # self.active_players_id = self.x[1]
        self.seasons=[
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
        self.stats= {
                    "Mecze zagrane":6,
                    "Mecze jako pierwsza 5":7,
                    "Minuty":8,
                    "Rzuty trafione":9,
                    "Rzuty oddane":10,
                    "Skuteczność rzutów":11,
                    "Rzuty za 3 trafione":12,
                    "Rzuty za 3 oddane":13,
                    "Skuteczność rzutów za 3":14,
                    "Rzuty z fauli trafione":15,
                    "Rzuty z fauli oddane":16,
                    "Skuteczność rzutów z fauli":17,
                    "Zbiórki w ataku":18,
                    "Zborki w defensywie":19,
                    "Zbiórki":20,
                    "Asysty":21,
                    "Kradzieże":22,
                    "Bloki":23,
                    "Straty":24,
                    "Faule osobiste":25,
                    "Punkty":26,
                }
        self.choosen_stat_idx = self.stats[self.choosen_stat]

    def pobierz_dane(self):

        # Pobieranie id gracza, którego użytkownik wybrał
        self.id1 = self.active_players_id[self.player1]
        self.id2 = self.active_players_id[self.player2]
        self.id3 = self.active_players_id[self.player3]

        # Pobieranie danych wybranych graczy
        self.career1 = playercareerstats.PlayerCareerStats(player_id=self.id1) 
        self.career2 = playercareerstats.PlayerCareerStats(player_id=self.id2) 
        self.career3 = playercareerstats.PlayerCareerStats(player_id=self.id3) 

        # Tworzenie słownika
        self.nba1=self.career1.get_dict()
        self.nba2=self.career2.get_dict()
        self.nba3=self.career3.get_dict()

        # Tworzenie list z danymi z ostatnich n sezonów (jeśli gracz nie był w tym czasie w lidze, to uzupełniamy listę Nullem)
        self.stat1 = []
        if len(self.nba1["resultSets"][2]["rowSet"]) >= self.seasons_countback:
            for i in range(len(self.nba1["resultSets"][2]["rowSet"])-self.seasons_countback,len(self.nba1["resultSets"][2]["rowSet"])):
                self.stat1.append(self.nba1["resultSets"][2]["rowSet"][i][self.choosen_stat_idx])
        else:
            for i in range(len(self.nba1["resultSets"][2]["rowSet"])):
                self.stat1.append(self.nba1["resultSets"][2]["rowSet"][i][self.choosen_stat_idx])
            for i in range(self.seasons_countback- len(self.nba1["resultSets"][2]["rowSet"])):
                self.stat1.insert(0,None)
        self.stat2 = []
        if len(self.nba2["resultSets"][2]["rowSet"]) >= self.seasons_countback:
            for i in range(len(self.nba2["resultSets"][2]["rowSet"])-self.seasons_countback,len(self.nba2["resultSets"][2]["rowSet"])):
                self.stat2.append(self.nba2["resultSets"][2]["rowSet"][i][self.choosen_stat_idx])
        else:
            for i in range(len(self.nba2["resultSets"][2]["rowSet"])):
                self.stat2.append(self.nba2["resultSets"][2]["rowSet"][i][self.choosen_stat_idx])
            for i in range(self.seasons_countback- len(self.nba2["resultSets"][2]["rowSet"])):
                self.stat2.insert(0,None)
        self.stat3 = []
        if len(self.nba3["resultSets"][2]["rowSet"]) >= self.seasons_countback:
            for i in range(len(self.nba3["resultSets"][2]["rowSet"])-self.seasons_countback,len(self.nba3["resultSets"][2]["rowSet"])):
                self.stat3.append(self.nba3["resultSets"][2]["rowSet"][i][self.choosen_stat_idx])
        else:
            for i in range(len(self.nba3["resultSets"][2]["rowSet"])):
                self.stat3.append(self.nba3["resultSets"][2]["rowSet"][i][self.choosen_stat_idx])
            for i in range(self.seasons_countback- len(self.nba3["resultSets"][2]["rowSet"])):
                self.stat3.insert(0,None)
        # Tworzenie listy n sezonów
        self.selected_seasons = []
        self.frame1 = self.career1.get_data_frames()[3]
        self.frame2 = self.career2.get_data_frames()[3]
        self.frame3 = self.career3.get_data_frames()[3]
        for i in range(self.seasons_countback,0,-1):
            self.selected_seasons.append(self.seasons[len(self.seasons)-i])        
        return self.stat1,self.stat2,self.stat3,self.active_players_full_name,self.active_players_id,self.id1,self.id2,self.id3,self.selected_seasons,self.frame1,self.frame2,self.frame3