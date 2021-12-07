a = IO.read('input/7').split(',').map(&:to_i);
puts 2000.times.collect {|counter| a.collect {|x| x > counter ? x - counter : counter - x }.sum }.sort.first
