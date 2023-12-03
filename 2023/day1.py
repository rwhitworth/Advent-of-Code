import re

f = open('day1input', 'r')

result = 0
DEBUG = 0

for input in f:
  numbers_only = re.sub('[^0-9]', '', input)
  if DEBUG: print(f"{numbers_only}\t", end='')
  num_numbers = len(numbers_only)

  if num_numbers == 1:
    numbers_only = f"{numbers_only}{numbers_only}"
    if DEBUG: print(f"{numbers_only}")
    result = result + int(numbers_only) 
  else:
    numbers_only = numbers_only[0] + numbers_only[num_numbers-1]
    if DEBUG: print(f"{numbers_only}")
    result = result + int(numbers_only)

print(f"result: {result}")
