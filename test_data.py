from ohmysportsfeedspy import MySportsFeeds
from cryptography.fernet import Fernet
import json

with open('key.txt', 'r') as myfile:
  key = myfile.read()
token = 'gAAAAABboJLxyuPbAIa6Nj6k-HXj_2MXHsParKmj3o24xzIBKwzoQ5SiNUr0ftawcfA0kklvX9j6Sceh3JoQMFUTKJEnhtnoFQ=='
f = Fernet(key)

msf = MySportsFeeds(version="1.1", store_type=None)

msf.authenticate("<76991493-077a-4a0f-92da-874b8c>", "<#{f.decrypt(token)}>")
output = msf.msf_get_data(league='nfl',season='2015-2016-regular',feed='cumulative_player_stats',format='json',team='dallas-cowboys')