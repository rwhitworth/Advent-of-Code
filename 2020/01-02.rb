a = IO.read('1').split("\n");
a = a.collect(&:to_i)
a.select {|x| a.select {|y| a.select {|z| puts "#{x} #{y} #{z}" if x + y + z == 2020; }; }; };
# this a bad solution.. next take the 3 numbers that are output (from any line, they're all the same) and multiply them together to get the final answer
