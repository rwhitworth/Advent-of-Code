a = IO.read('input/2').split("\n");
x = a.collect {|x| x.split(' ')[1].to_i if x.split(' ')[0] == 'forward' }.select {|x| !x.nil? }.sum;
z = a.collect {|x| x.split(' ')[1].to_i if x.split(' ')[0] == 'down' }.select {|x| !x.nil? }.sum - a.collect {|x| x.split(' ')[1].to_i if x.split(' ')[0] == 'up' }.select {|x| !x.nil? }.sum;
x * z
