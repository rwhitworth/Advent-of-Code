require 'set'

input = File.readlines('day4input.txt', chomp: true)
            .map { _1.scan(/\d+/) }
            .map { [Set.new(_1[0].._1[1]), Set.new(_1[2].._1[3])] }

puts solution1 = input.count { (_1[0] <= _1[1]) || (_1[0] >= _1[1]) }

puts solution2 = input.count { (_1[0].intersect? _1[1]) }
