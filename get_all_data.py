from ohmysportsfeedspy import MySportsFeeds
from cryptography.fernet import Fernet
import json

with open('key.txt', 'r') as myfile:
  key = myfile.read()
f = Fernet(key)
token = 'gAAAAABboxejr3hkCDwGeNSEQDPjLbw2T-M41JclD-7ZqqhZWAM61cjqybisLMBFdARpk4L0NsX90tpRNabJcr-oP31W--eiqcbbE8Qe5ZOz9273CdNy5Ts='

msf = MySportsFeeds(version="2.0", store_type='file', store_location='results/')

msf.authenticate(f.decrypt(token), "MYSPORTSFEEDS")
#output = msf.msf_get_data(league='mlb',season='2016-playoff',feed='seasonal_games',format='json')
#print output
league = 'nfl'
beg_yr = 2014
end_yr = 2019
rec_plyff = False
valid_feeds = [
            'seasonal_games',
            'daily_games',
            'weekly_games',
            'seasonal_dfs',
            'daily_dfs',
            'weekly_dfs',
            'seasonal_player_gamelogs',
            'daily_player_gamelogs',
            'weekly_player_gamelogs',
            'seasonal_team_gamelogs',
            'daily_team_gamelogs',
            'weekly_team_gamelogs',
            'game_boxscore',
            'game_playbyplay',
            'game_lineup',
            'current_season',
            'player_injuries',
            'latest_updates',
            'seasonal_team_stats',
            'seasonal_player_stats',
            'seasonal_venues',
            'players',
            'seasonal_standings'
        ]
valid_types = ['regular', 'playoff']

for feed in valid_feeds:
	for type in valid_types:
		for year in range(beg_yr, end_yr+1):
			if not(year == beg_yr and type == 'playoff') and not(year == end_yr and type == 'playoff' and not rec_plyff):
				try:
					msf.msf_get_data(league=league,season=str(year)+'-'+type,feed=feed,format='json')
				except:
					print 'failure on ' + feed + ' ' + str(year) + ' ' + type