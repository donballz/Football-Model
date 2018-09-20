from ohmysportsfeedspy import MySportsFeeds
from cryptography.fernet import Fernet
import json

msf = MySportsFeeds(version="2.0", store_type='file', store_location='results/')

msf.authenticate("76991493-077a-4a0f-92da-874b8c", "MYSPORTSFEEDS")
output = msf.msf_get_data(league='mlb',season='2016-playoff',feed='seasonal_games',format='json')
print output