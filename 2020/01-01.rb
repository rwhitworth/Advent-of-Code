a = IO.read('input/1').split("\n");
q = a.select {|x| b = a.select {|y| y.to_i + x.to_i == 2020 }; [b,x] if b.count > 0; }
q[0].to_i * q[1].to_i
