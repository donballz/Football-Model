from ohmysportsfeedspy import MySportsFeeds
from cryptography.fernet import Fernet
# Put this somewhere safe!
with open('key.txt', 'r') as myfile:
  key = myfile.read()
token = 'gAAAAABboJLxyuPbAIa6Nj6k-HXj_2MXHsParKmj3o24xzIBKwzoQ5SiNUr0ftawcfA0kklvX9j6Sceh3JoQMFUTKJEnhtnoFQ=='
f = Fernet(key)

msf = MySportsFeeds(version="1.0")

msf.authenticate("836f3af8-933a-49ed-a37b-fbe37b", f.decrypt(token))
output = msf.msf_get_data(league='nba',season='2016-2017-regular',feed='player_gamelogs',format='json',player='stephen-curry')