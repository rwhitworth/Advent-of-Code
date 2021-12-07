a = IO.read('input/6').split(',').collect {|x| x.to_i };
q = 9.times.collect {|x| 0 }
a.each do |x|
  q[x] = q[x] + 1
end;
256.times do |count|
  # 9 total buckets, but bucket 0 is not really processed, it just gets trashed
  old_zero = q[0]

  8.times do |counter2|
    q[counter2] = q[counter2 + 1]
  end

  q[8] = old_zero
  q[6] = q[6] + old_zero
end;

q.sum
