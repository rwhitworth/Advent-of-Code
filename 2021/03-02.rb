a = IO.read('input/3').split("\n");
len = a[0].length
(0..len-1).each do |loop|
  bits = a.collect {|x| x[loop]};
  ones = bits.select {|x| x == '1'}.count;
  if ones < (bits.count - ones)
    a = a.select {|x| x if x[loop] == '0' }
  else
    a = a.select {|x| x if x[loop] == '1' }
  end
end
most_common = a[0];

a = IO.read('input/3').split("\n");
len = a[0].length
(0..len-1).each do |loop|
  bits = a.collect {|x| x[loop]};
  ones = bits.select {|x| x == '1'}.count;
  if ones < (bits.count - ones)
    a = a.select {|x| x if x[loop] == '1' }
  else
    a = a.select {|x| x if x[loop] == '0' }
  end
  break if a.count == 1
end
least_common = a[0];

most_common.to_i(2) * least_common.to_i(2)
