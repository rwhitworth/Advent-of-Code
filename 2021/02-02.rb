x = 0;
z = 0;
aim = 0;
a = IO.read('input/2').split("\n");

def process(n, x, z, aim)
  cmd = n.split(' ')[0];
  num = n.split(' ')[1].to_i;
  aim += num if cmd == 'down'
  aim -= num if cmd == 'up'
  x += num if cmd == 'forward'
  z += aim * num if cmd == 'forward'
  [x, z, aim]
end

a.each do |loop|
  x, z, aim = process(loop, x, z, aim)
end;

x * z
