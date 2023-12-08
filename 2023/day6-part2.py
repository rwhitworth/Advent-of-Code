import re

f = open('day6input', 'r')

result = 1
times = []
distances = []
DEBUG = 0

input = f.readline()
input = input.replace("\n", '')
input = re.sub('(.*?):\s{1,10}', '', input)
input = re.sub('\s{1,10}', ' ', input)
times = input.split(' ')

input = f.readline()
input = input.replace("\n", '')
input = re.sub('(.*?):\s{1,10}', '', input)
input = re.sub('\s{1,10}', ' ', input)
distances = input.split(' ')

real_time = ''
real_dist = ''

for i in range(0, len(times)):
  real_time = real_time + times[i]
  real_dist = real_dist + distances[i]

times = [real_time]
distances = [real_dist]

for i in range(0, len(times)):
  winning = 0
  time = int(times[i])
  distance = int(distances[i])
  if DEBUG: print(f'time: {times} \tdistance: {distance}')
  for h in range(1, time + 1):
    r = (h * time) - (h * h)
    if r > distance:
      winning += 1
  if DEBUG: print(f'winning: {winning}')
  result *= winning

print(f"result: {result}")