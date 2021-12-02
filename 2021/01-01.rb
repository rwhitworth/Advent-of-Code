a = IO.read('input/1').split("\n");
a.select.with_index {|n, i| true if a[i].to_i < a[i+1].to_i }.count
