# frozen_string_literal: true

# Advent of Code 2022, Day 2
# Part 1: 
# Part 2: 

sample_data = "A Y
B X
C Z"
sample_p1_answer = 15
sample_p2_answer = 12

$score = {
  "A X" => 3+1,
  "B X" => 0+1,
  "C X" => 6+1,
  "A Y" => 8,
  "B Y" => 3+2,
  "C Y" => 0+2,
  "A Z" => 3,
  "B Z" => 9,
  "C Z" => 6
}

$score2 = {
  "A X" => 3,
  "B X" => 1,
  "C X" => 2,
  "A Y" => 4,
  "B Y" => 5,
  "C Y" => 6,
  "A Z" => 8,
  "B Z" => 9,
  "C Z" => 7
}
def test_equal?(left, right)
  if left != right 
    print left
    puts ''
    print right
    puts ''
    puts "FAIL"
    return false
  else
    puts "PASS"
    return true
  end
end

def parse_data(data_string)
  data_string.split("\n")
end

def part1(data_string)
#  print $score
#  print parse_data(data_string)
  parse_data(data_string).map { |s| $score[s]}.sum
end

def part2(data_string)
  parse_data(data_string).map { |s| $score2[s]}.sum
end

puts '-- Tests --'
test_equal?(parse_data(sample_data), ["A Y", "B X", "C Z"])
# A = Rock, B = Paper, C = Scissor
# X = Rock, Y = Paper, Z = Scissor
#   = 1pt     = 2pts     = 3pts
test_equal?($score["A X"], 3+1)
test_equal?($score["B X"], 0+1)
test_equal?($score["C X"], 6+1)
test_equal?($score["A Y"], 8)
test_equal?($score["B Y"], 3+2)
test_equal?($score["C Y"], 0+2)
test_equal?($score["A Z"], 0+3)
test_equal?($score["B Z"], 6+3)
test_equal?($score["C Z"], 6)
# X = Lose, Y = Draw, Z = Win
#   = 0pt     = 3pts    = 6pts
test_equal?($score2["A X"], 3+0)
test_equal?($score2["B X"], 1) # 1+0
test_equal?($score2["C X"], 2+0)
test_equal?($score2["A Y"], 4) # 1+3
test_equal?($score2["B Y"], 2+3)
test_equal?($score2["C Y"], 3+3)
test_equal?($score2["A Z"], 2+6)
test_equal?($score2["B Z"], 3+6)
test_equal?($score2["C Z"], 7) # 1+6
test_equal?(part1(sample_data), sample_p1_answer)
test_equal?(part2(sample_data), sample_p2_answer)
puts '-----------'
#------

data = File.read('day2input.txt')

puts "\nPart 1"
puts part1(data)

puts "\nPart 2"
puts part2(data)

