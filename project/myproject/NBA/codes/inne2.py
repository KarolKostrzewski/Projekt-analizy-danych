from nba_api.stats.static import players
player_list=players.get_active_players()
player1 ='LeBron James'
seasons_countback=7
choosen_stat ='FG_PCT'
seasons=['2000-01','2001-02','2002-03','2003-04','2004-05','2005-06','2006-07','2007-08','2008-09','2009-10','2010-11','2011-12','2012-13','2013-14','2014-15','2015-16','2016-17','2017-18','2018-19','2019-20','2020-21','2021-22','2022-23']
list_of_stats=['GP','GS','MIN','FGM','FGA','FG_PCT','FG3M','FG3A','FG3_PCT','FTM','FTA','FT_PCT','OREB','DREB','REB','AST','STL','BLK','TOV','PF','PTS']
stats= {"GP":6,"GS":7,"MIN":8,"FGM":9,"FGA":10,"FG_PCT":11,"FG3M":12,"FG3A":13,"FG3_PCT":14,"FTM":15,"FTA":16,"FT_PCT":17,"OREB":18,"DREB":19,"REB":20,"AST":21,"STL":22,"BLK":23,"TOV":24,"PF":25,"PTS":26,}
