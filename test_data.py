from ohmysportsfeedspy import MySportsFeeds
from cryptography.fernet import Fernet
import json

with open('key.txt', 'r') as myfile:
  key = myfile.read()
f = Fernet(key)
token = 'gAAAAABboxejr3hkCDwGeNSEQDPjLbw2T-M41JclD-7ZqqhZWAM61cjqybisLMBFdARpk4L0NsX90tpRNabJcr-oP31W--eiqcbbE8Qe5ZOz9273CdNy5Ts='

msf = MySportsFeeds(version="2.0", store_type='file', store_location='results/')

msf.authenticate(f.decrypt(token), "MYSPORTSFEEDS")
output = msf.msf_get_data(league='nba',season='2016-playoff',feed='seasonal_games',format='json')
print output