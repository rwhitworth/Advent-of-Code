import re

f = open('day4input', 'r')

result = 0
DEBUG = 0
POINTS = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]

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
  
  if DEBUG: print(f'{result} + {POINTS[card_score]}')
  result += POINTS[card_score]

print(f"result: {result}")
