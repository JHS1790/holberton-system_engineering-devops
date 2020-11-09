#!/usr/bin/env ruby

#match = /Holberton/.match(ARGV[0])
match = ARGV[0].scan(/hbt+n/)
for i in 0 ... match.length
    print "#{match[i]}"
end
puts