#
#
# Note: You don't have enough RAM to run this solution. You don't.
# So.. while I believe this code works (it works on the sample input!)
# I don't believe this is functional in reality
#
# The proper way to solve the problem is dynamically handle the slices
# But I really don't feel like coding that solution right now. 
#
# Real life > Advent of Code
#
#


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

for input in f:
  input = input.replace("\n", '')
  # print(f'input: {input}')

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
    r = re.search('([0-9]{1,10}) ([0-9]{1,10}) ([0-9]{1,10})', input)
    dst = r.group(1)
    src = r.group(2)
    count = r.group(3)
    seed_to_soil[dst] = [src, dst, count]

  if block == 'soil-to-fertilizer map':
    r = re.search('([0-9]{1,10}) ([0-9]{1,10}) ([0-9]{1,10})', input)
    dst = r.group(1)
    src = r.group(2)
    count = r.group(3)
    soil_to_fert[dst] = [src, dst, count]

  if block == 'fertilizer-to-water map':
    r = re.search('([0-9]{1,10}) ([0-9]{1,10}) ([0-9]{1,10})', input)
    dst = r.group(1)
    src = r.group(2)
    count = r.group(3)
    fert_to_water[dst] = [src, dst, count]

  if block == 'water-to-light map':
    r = re.search('([0-9]{1,10}) ([0-9]{1,10}) ([0-9]{1,10})', input)
    dst = r.group(1)
    src = r.group(2)
    count = r.group(3)
    water_to_light[dst] = [src, dst, count]

  if block == 'light-to-temperature map':
    r = re.search('([0-9]{1,10}) ([0-9]{1,10}) ([0-9]{1,10})', input)
    dst = r.group(1)
    src = r.group(2)
    count = r.group(3)
    light_to_temp[dst] = [src, dst, count]

  if block == 'temperature-to-humidity map':
    r = re.search('([0-9]{1,10}) ([0-9]{1,10}) ([0-9]{1,10})', input)
    dst = r.group(1)
    src = r.group(2)
    count = r.group(3)
    temp_to_hum[dst] = [src, dst, count]

  if block == 'humidity-to-location map':
    r = re.search('([0-9]{1,10}) ([0-9]{1,10}) ([0-9]{1,10})', input)
    dst = r.group(1)
    src = r.group(2)
    count = r.group(3)
    hum_to_loc[dst] = [src, dst, count]

def map_it(map, val):
  for item in map:
    item = map[item]
    if DEBUG: print(f'{item}')
    if val >= int(item[0]):
      if val <= (int(item[0]) + int(item[2])):
        return val - int(item[0]) + int(item[1])
  return val

for seed in seeds:
  temp = int(seed)

  if DEBUG: print(f'temp: {temp}')
  temp = map_it(seed_to_soil, temp)
  if DEBUG: print(f'temp: {temp}')
  temp = map_it(soil_to_fert, temp)
  if DEBUG: print(f'temp: {temp}')
  temp = map_it(fert_to_water, temp)
  if DEBUG: print(f'temp: {temp}')
  temp = map_it(water_to_light, temp)
  if DEBUG: print(f'temp: {temp}')
  temp = map_it(light_to_temp, temp)
  if DEBUG: print(f'temp: {temp}')
  temp = map_it(temp_to_hum, temp)
  if DEBUG: print(f'temp: {temp}')
  temp = map_it(hum_to_loc, temp)
  if DEBUG: print(f'temp: {temp}')

#   if temp in seed_to_soil:
#     temp = seed_to_soil[temp]
#   if temp in soil_to_fert:
#     temp = soil_to_fert[temp]
#   if temp in fert_to_water:
#     temp = fert_to_water[temp]
#   if temp in water_to_light:
#     temp = water_to_light[temp]
#   if temp in light_to_temp:
#     temp = light_to_temp[temp]
#   if temp in temp_to_hum:
#     temp = temp_to_hum[temp]
#   if temp in hum_to_loc:
#     temp = hum_to_loc[temp]

  if temp < result:
    result = temp
  
  if DEBUG: print(f'seed: {seed} - temp: {temp} - result: {result}')

print(f"result: {result}")