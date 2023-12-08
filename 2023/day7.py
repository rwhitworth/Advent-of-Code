import re

f = open('day7input', 'r')

result = 0
DEBUG = 0

directions = ''
locations = {}
current_location = 'AAA'
b = True

directions = f.readline().replace("\n", '')

for input in f:
  input = input.replace("\n", '')

  if len(input) < 3:
    continue

  r = re.search('([A-Za-z0-9]{3}) = \(([A-Za-z0-9]{3}), ([A-Za-z0-9]{3})\)', input)
  if r == None:
    print(f'ERROR: parsing went wrong 1')
  
  if r.groups() == None:
    print(f'ERROR: parsing went wrong 2')

  start = r.group(1)
  left = r.group(2)
  right = r.group(3)

  locations[start] = [left, right]

while b:
  for direction in directions:
    if DEBUG: print(f'start - current_location: {current_location}')
    if direction == 'L':
      if DEBUG: print('L')
      current_location = locations[current_location][0]
    if direction == 'R':
      if DEBUG: print('R')      
      current_location = locations[current_location][1]
    
    result += 1
    if DEBUG: print(f'stop  - current_location: {current_location}')

    if current_location == 'ZZZ':
      b = False
      break

print(f"result: {result}")