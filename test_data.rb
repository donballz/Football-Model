require "mysportsfeeds"
require_relative 'StringFind.rb'

PATH = '/Users/donald/Google Drive/Football Model'

msf = MySportsFeeds.new(version="1.0", true)
pwd = "8FAA0016D0D3EA6D4C70ED24A07C8B64"
key = File.read("#{PATH}/key.txt")

msf.authenticate("donballz", pwd.decrypt(key))

data = msf.msf_get_data('nfl', '2015-2016-regular', 'cumulative_player_stats', 'json', 'team' => 'detroit-lions')