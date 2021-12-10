PAIRS = [
  %q{[]},
  %q{{}},
  %q{<>},
  %q{()}
]
a = IO.read('input/10').split("\n");

def openings
  PAIRS.collect {|x| x[0] }
end

def opening?(letter)
  openings.any?(letter)
end

def closings
  PAIRS.collect {|x| x[1] }
end

def closing?(letter)
  closings.any?(letter)
end

# finds the matching open letter for a close character
def match_char(letter)
  PAIRS.select {|x| x[1] == letter }.last[0]
end

def points(letter)
  p = {
    ')' => 3,
    ']' => 57,
    '}' => 1197,
    '>' => 25137
  }
  p[letter]
end

def points_per_line(line)
  queue = []
  total_points = 0
  line.split('').each do |letter|
    if opening?(letter)
      queue.append(letter)
    end
    if closing?(letter)
      if queue.last == match_char(letter)
        queue.pop
      else
        total_points += points(letter)
        break
      end
    end
  end
  total_points
end

a.collect {|line| points_per_line(line) }.sum
