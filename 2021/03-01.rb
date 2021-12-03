a = IO.read('input/3').split("\n");
def q(a, pos)
  bits = a.collect {|x| x[pos]};
  ones = bits.select {|x| x == '1'}.count;
  total = a.count;
  return "0" if (total - ones) > ones
  "1"
end
most_common = (q(a, 0) + q(a, 1) + q(a, 2) + q(a, 3) + q(a, 4) + q(a, 5) + q(a, 6) + q(a, 7) + q(a, 8) + q(a, 9) + q(a, 10) + q(a, 11)).to_i(2);
def q(a, pos)
  bits = a.collect {|x| x[pos]};
  ones = bits.select {|x| x == '1'}.count;
  total = a.count;
  return "1" if (total - ones) > ones
  "0"
end
least_common = (q(a, 0) + q(a, 1) + q(a, 2) + q(a, 3) + q(a, 4) + q(a, 5) + q(a, 6) + q(a, 7) + q(a, 8) + q(a, 9) + q(a, 10) + q(a, 11)).to_i(2);
most_common * least_common
