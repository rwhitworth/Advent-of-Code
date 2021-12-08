# I'm particularly proud of how ugly this one is
puts IO.read('input/8').split("\n").collect {|x| x.split("|")[1] }.join(' ').split(' ').sort.collect {|x| [x, x.length] }.select {|x| [2,3,4,7].include?(x[1]) }.count
