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
  for game in games:
    # print(f'game: {game}')
    cubes = re.findall('.*?(\d{1,3} [a-zA-Z]{3,5}).*?', game)
    invalid_cube = int(game_num)
    for cube in cubes:
      #if DEBUG: print(f'cube: {cube}')
      cube_re = re.search('.*?([0-9]{1,3}) ([a-zA-Z]{3,5}).*?', cube)
      if cube_re is None:
        print('ERROR: cube_re no results')
        invalid_cube = 0
        break
      if cube_re.group(2) == 'red': 
        if int(cube_re.group(1)) > 12:
          if DEBUG: print(f'invalid cube: {cube}')
          invalid_cube = 0
          break
      elif cube_re.group(2) == 'green': 
        if int(cube_re.group(1)) > 13:
          if DEBUG: print(f'invalid cube: {cube}')
          invalid_cube = 0
          break
      elif cube_re.group(2) == 'blue': 
        if int(cube_re.group(1)) > 14:
          if DEBUG: print(f'invalid cube: {cube}')
          invalid_cube = 0
          break
      else:
        print(f'ERROR: cube_re found {cube_re.group(2)}')
        invalid_cube = 0
        break

    if invalid_cube == 0:
      break

  result = result + invalid_cube

print(f"result: {result}")
