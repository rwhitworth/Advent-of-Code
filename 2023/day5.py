import re

f = open('day5input', 'r')

result = 1000000000 * 10000000
DEBUG = 0

seed_to_soil = {}
soil_to_fert = {}
fert_to_water = {}
water_to_light = {}
light_to_temp = {}
temp_to_hum = {}
hum_to_loc = {}

seeds = []
block = ''

def create_map_line(input):
  r = re.search('([0-9]{1,10}) ([0-9]{1,10}) ([0-9]{1,10})', input)
  dst = r.group(1)
  src = r.group(2)
  count = r.group(3)
  return dst, [src, dst, count]

def map_it(map, val):
  for item in map:
    item = map[item]
    if val >= int(item[0]):
      if val <= (int(item[0]) + int(item[2])):
        return val - int(item[0]) + int(item[1])
  return val

for input in f:
  input = input.replace("\n", '')

  if len(input) < 3:
    continue

  r = re.search('(.*)?:', input)
  if r != None:
    if r.groups() != None:
      block = r.group(1)
      continue

  if block == 'seeds':
    seeds = input.replace("\n", '').split(' ')

  if block == 'seed-to-soil map':
    dst, map_line = create_map_line(input)
    seed_to_soil[dst] = map_line

  if block == 'soil-to-fertilizer map':
    dst, map_line = create_map_line(input)
    soil_to_fert[dst] = map_line

  if block == 'fertilizer-to-water map':
    dst, map_line = create_map_line(input)
    fert_to_water[dst] = map_line

  if block == 'water-to-light map':
    dst, map_line = create_map_line(input)
    water_to_light[dst] = map_line

  if block == 'light-to-temperature map':
    dst, map_line = create_map_line(input)
    light_to_temp[dst] = map_line

  if block == 'temperature-to-humidity map':
    dst, map_line = create_map_line(input)
    temp_to_hum[dst] = map_line

  if block == 'humidity-to-location map':
    dst, map_line = create_map_line(input)
    hum_to_loc[dst] = map_line


for seed in seeds:
  temp = int(seed)

  temp = map_it(seed_to_soil, temp)
  temp = map_it(soil_to_fert, temp)
  temp = map_it(fert_to_water, temp)
  temp = map_it(water_to_light, temp)
  temp = map_it(light_to_temp, temp)
  temp = map_it(temp_to_hum, temp)
  temp = map_it(hum_to_loc, temp)

  if temp < result:
    result = temp
  
  if DEBUG: print(f'seed: {seed} - temp: {temp} - result: {result}')

print(f"result: {result}")