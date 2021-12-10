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

# in retrospect, should be named 'keep'
def discard(line)
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
  return false if total_points > 0
  true if total_points == 0
end

def missing_closures(line)
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
        puts '======='
        puts "SOMETHING WENT WRONG - #{letter}"
      end
    end
  end
  queue
end

def new_points(line)
  p = {
    '(' => 1,
    '[' => 2,
    '{' => 3,
    '<' => 4
  }
  res = line.split('').collect {|x| p[x]}
  puts res
  total_score = 0
  res.each do |x|
    total_score *= 5
    total_score += x
  end
  total_score
end

valid_lines = a.select {|line| discard(line) };

missing_values = valid_lines.collect {|x| new_points(missing_closures(x).join.reverse) };

puts missing_values.sort[(missing_values.count / 2)]
