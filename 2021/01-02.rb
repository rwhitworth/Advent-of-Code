a = IO.read('input/1').split("\n");

def q(a, num)
  a[num].to_i + a[num + 1].to_i + a[num + 2].to_i
end

a.select.with_index {|n, i| q(a, i) < q(a, i + 1) }.count
