#
#
# This one doesn't work. I'm not super interested in figuring it out at this point. Recursion is difficult.
#
# Real life > Advent of Code
#
#


import re
import unittest

f = open('day4input-test', 'r')

result = 0
DEBUG = 1
POINTS = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]

score_per_line = []
score_per_line.append(1)

def recurse(arr, recur=0):
  assert len(arr) > 0
  
  res = 0
  
  while len(arr) > 0:
    if DEBUG: print(f'len(arr): {len(arr)} - arr: {arr} - res: {res}')
    i = arr.pop(0)
    if i > 0:
      res += 1
    if i > 1 and len(arr) > 0:
      if DEBUG: print(f'i: {i} - len(arr): {len(arr)}')
      for j in range(1, i):
        if DEBUG: print(f'arr: {arr}')
        res += recurse(arr.copy())
  if DEBUG: print(f'returning res: {res}')
  return res

# assert recurse([0]) == 0
# assert recurse([1]) == 1
# assert recurse([2]) == 1
# assert recurse([3]) == 1
# assert recurse([2,0]) == 1
# assert recurse([1,1]) == 2
# if DEBUG: print(f'recurse([0,1]): {recurse([0,1])}')
# assert recurse([0,1]) == 1
# if DEBUG: print(f'recurse([2,2]): {recurse([2,2])}')
# assert recurse([2,2]) == 3
# assert recurse([0, 0, 0]) == 0
# assert recurse([1, 0, 0]) == 1
# assert recurse([0, 1, 0]) == 1
# assert recurse([0, 0, 1]) == 1
# assert recurse([0, 1, 1]) == 2
# assert recurse([1, 1, 1]) == 3
assert recurse([2, 1, 1]) == 3
# if DEBUG: print('====')
# if DEBUG: print(f'recurse([1, 4, 2, 2, 1, 0, 0]): {recurse([1, 4, 2, 2, 1, 0, 0])}')
# if DEBUG: print("====\n\n")
# assert recurse([1, 4, 2, 2, 1, 0, 0]) == 30

for input in f:
  input = input.replace('  ', ' ').replace("\n", '')
  r = re.search('Card ([0-9\s]{1,4}): ([0-9\s]{1,30}) \| ([0-9\s]{1,100})', input)

  if DEBUG: print(f'Card: {r.group(1)}')

  winners = r.group(2).split(' ')
  numbers = r.group(3).split(' ')

  card_score = 0
  for i in numbers:
    if i in winners:
      card_score += 1
      if DEBUG: print(f'{winners} - {numbers}')
  
  score_per_line.append(card_score)

print(f'{score_per_line}')



print(f"result: {result}")
