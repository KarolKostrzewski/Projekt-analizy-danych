from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players
import nba_ustawienia as u
import pandas as pd
import matplotlib.pyplot as plt

# Tworzenie klasy, która zbiera dane, przetwarza i rysuje wykres
class Dane:

    def __init__(self):
        self.player1 = u.player1
        self.player2 = u.player2
        self.player3 = u.player3
        self.seasons_countback = u.seasons_countback
        self.seasons = u.seasons
        self.choosen_stat = u.choosen_stat
        self.choosen_stat_idx = u.stats[self.choosen_stat]
    
    def pobierz_dane(self):
        # Pobranie listy aktywnych graczy
        self.player_list = players.get_active_players()
        # Tworzenie listy aktywnych graczy po full_name isłownika z full_name i id gdzie kluczem jest full_name
        self.active_players_full_name = []
        self.active_players_id = dict()

        for i in range(len(self.player_list)):
            full_name = self.player_list[i]['full_name']
            id = self.player_list[i]['id']
            self.active_players_full_name.append(full_name)
            self.active_players_id[full_name]=id

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
        return self.stat1,self.stat2,self.stat3,self.active_players_full_name,self.active_players_id,self.id1,self.id2,self.id3


    def pobierz_liste_sezonow(self):
        # Tworzenie listy n sezonów
        self.selected_seasons = []
        for i in range(self.seasons_countback,0,-1):
            self.selected_seasons.append(self.seasons[len(self.seasons)-i])
        return self.selected_seasons


    def zrob_wykres(self):
        # Tworzenie ramki danych za pomocą pandas
        df = pd.DataFrame({'Daty': self.selected_seasons, 'Punkty gracza 1': self.stat1, 'Punkty gracza 2': self.stat2, 'Punkty gracza 3': self.stat3})

        # Tworzenie wykresu liniowego
        plt.plot(df['Daty'], df['Punkty gracza 1'], label=self.player1)
        plt.plot(df['Daty'][:len(self.stat2)], df['Punkty gracza 2'], label=self.player2)
        plt.plot(df['Daty'][:len(self.stat3)], df['Punkty gracza 3'], label=self.player3)

        # Konfiguracja wykresu
        plt.xlabel('Sezony')
        plt.ylabel('Punkty')
        plt.title('Porównanie punktów graczy w wybranych sezonach')
        plt.legend()

        # Wyświetlanie wykresu
        plt.show()

    def zrob_tabele(self):

        print(self.career1.get_data_frames()[0])
        print(self.career2.get_data_frames()[0])
        print(self.career3.get_data_frames()[0])

    def career(self):
        print(self.career1.get_data_frames()[1])
        print(self.career2.get_data_frames()[1])
        print(self.career3.get_data_frames()[1])

x=Dane()
y=x.pobierz_dane()
# x.pobierz_liste_sezonow()
# x.zrob_wykres()
# x.zrob_tabele()
# x.career()
print(y[0])