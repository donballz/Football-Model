from ohmysportsfeedspy import MySportsFeeds
from cryptography.fernet import Fernet
# Put this somewhere safe!
with open('key.txt', 'r') as myfile:
  key = myfile.read()
token = 'gAAAAABboJLxyuPbAIa6Nj6k-HXj_2MXHsParKmj3o24xzIBKwzoQ5SiNUr0ftawcfA0kklvX9j6Sceh3JoQMFUTKJEnhtnoFQ=='
f = Fernet(key)

msf = MySportsFeeds(version="1.2")

msf.authenticate("836f3af8-933a-49ed-a37b-fbe37b", f.decrypt(key))
output = msf.msf_get_data(league='nfl',season='2015-2016-regular',feed='cumulative_player_stats',format='xml',team='dallas-cowboys')
