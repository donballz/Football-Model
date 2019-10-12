require 'json'

json = File.read('results/current_season-nfl-2014-regular.json')
objt = JSON.parse(json)

def print_any(objt, lev)
	tab = '  '
	if objt.kind_of? Array
		objt.each { |x| print_any(x, lev + 1) }
	elsif objt.kind_of? Hash
		objt.each do |x,y| 
			puts (tab * lev) + x
			print_any(y, lev + 1) 
		end
	else 
		puts (tab * lev) + objt
	end
end
'''
objt.each do |k,v|
	if v.kind_of? Array
		v.each { |x| puts x }
	else
		puts v
	end
end
'''
print_any(objt,0)