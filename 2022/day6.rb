# frozen_string_literal: true

# Advent of Code 2022, Day 6
# Part 1: count characters until set of 4 differnt characters
# Part 2: 

sample_data1 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
sample_p1_answer1 = 5
sample_p2_answer1 = 23 
sample_data2 = "nppdvjthqldpwncqszvftbrmjlhg"
sample_p1_answer2 = 6
sample_data3 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
sample_p1_answer3 = 10
sample_data4 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
sample_p1_answer4 = 11

def test_equal?(left, right)
  if left != right
    print left, "\n"
    print right, "\n"
    puts 'FAIL'
    false
  else
    puts 'PASS'
    true
  end
end

def parse_data(data_string)
  # return array of characters
  data_string.chars
end

def unique?(chars)
  return true if chars.length == chars.uniq.length
  false
end
  
def part1(data_string)
  datastream = parse_data(data_string)
  datastream.each_index { |i| 
    return i+4 if unique?(datastream[i, 4]) }
end

def part2(data_string)
  datastream = parse_data(data_string)
  datastream.each_index { |i| 
    return i+14 if unique?(datastream[i, 14]) }
end

puts '-- Tests --'
test_equal?(parse_data(sample_data1), ["b", "v", "w", "b", "j", "p", "l", "b", "g", "v", "b", "h", "s", "r", "l", "p", "g", "d", "m", "j", "q", "w", "f", "t", "v", "n", "c", "z"])

test_equal?(unique?(["a", "b", "c", "d"]), true)
test_equal?(unique?("abcd".chars), true)
test_equal?(unique?("abca".chars), false)
test_equal?(part1(sample_data1), sample_p1_answer1)

#split data into groups of three

test_equal?(part2(sample_data1), sample_p2_answer1)
puts '-----------'

# ------

data = File.read('day6input.txt')

puts "\nPart 1"
puts part1(data)

puts "\nPart 2"
puts part2(data)
