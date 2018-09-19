require "mysportsfeeds"
require_relative 'StringFind.rb'

PATH = '/Users/donald/Projects/Football-Model'

msf = MySportsFeeds.new(version="1.0", true)
pwd = "2F6F490793BE248DE3B200CF16C545A0"
key = File.read("#{PATH}/key.txt")

msf.authenticate("810ff31c-e7ca-4926-a717-0bef77", pwd.decrypt(key))

data = msf.msf_get_data('nfl', '2015-2016-regular', 'cumulative_player_stats', 'json', 'team' => 'detroit-lions')