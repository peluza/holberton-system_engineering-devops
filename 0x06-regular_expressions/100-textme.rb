#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(\+?\w+)\]\s\[to:(\+\d{1,})\]\s\[flags:(-?\d{1}:-?\d:-?\d:-?\d:-?\d)\]/).join(",")