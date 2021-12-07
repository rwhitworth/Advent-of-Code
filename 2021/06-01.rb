a = IO.read('input/6').split(',').collect {|x| x.to_i };
q = 9.times.collect {|x| 0 }
a.each do |x|
  q[x] = q[x] + 1
end;
80.times do |count|
  # 9 total buckets, but bucket 0 is not really processed, it just gets trashed
  old_zero = q[0]

  8.times do |counter2|
    q[counter2] = q[counter2 + 1]
  end

  q[8] = old_zero
  q[6] = q[6] + old_zero
end;

q.sum



# first solution is below, but it has a major drawback in regard to runtime speed
# the above solution uses a handful of buckets and has many fewer memory allocations

#def age_fish(school)
#  growth = 0
#  res = school.collect do |fish|
#    if fish == 0
#      growth = growth + 1
#      6
#    else
#      fish - 1
#    end
#  end
#  [res, growth]
#end

## example input
## a = '3,4,3,1,2'.split(',').collect {|x| x.to_i };
#a = IO.read('input/6').split(',').collect {|x| x.to_i };

#80.times do |count|
#  res, growth = age_fish(a);
#  growth.times do |counter2|
#    res << 8
#  end
#  a = res
#end

#puts a.count
