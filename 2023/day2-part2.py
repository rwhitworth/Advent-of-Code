import re

f = open('day2input', 'r')

result = 0
DEBUG = 0

for input in f:
  #if DEBUG: print(input, end='')
  r = re.search('Game ([0-9]{1,3}): (.*)', input)
  if r is None:
    print('ERROR: No match')
  game_num = r.group(1)
  games = r.group(2)
  if DEBUG: print(f'Game: {game_num} - {games}')
  games = games.split(';')
  red = blue = green = 1
  for game in games:
    cubes = re.findall('.*?(\d{1,3} [a-zA-Z]{3,5}).*?', game)
    for cube in cubes:
      if DEBUG: print(f'cube: {cube}')
      cube_re = re.search('.*?([0-9]{1,3}) ([a-zA-Z]{3,5}).*?', cube)
      if cube_re is None:
        print('ERROR: cube_re no results')
        break
      if cube_re.group(2) == 'red': 
        if int(cube_re.group(1)) > red:
          red = int(cube_re.group(1))
      elif cube_re.group(2) == 'green': 
        if int(cube_re.group(1)) > green:
          green = int(cube_re.group(1))
      elif cube_re.group(2) == 'blue': 
        if int(cube_re.group(1)) > blue:
          blue = int(cube_re.group(1))
      else:
        print(f'ERROR: cube_re found {cube_re.group(2)}')
        break
  if DEBUG: print(f'{red} {green} {blue}')
  result = result + (red * green * blue)

print(f"result: {result}")
