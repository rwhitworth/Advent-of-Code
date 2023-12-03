import re

f = open('day1input', 'r')

result = 0
DEBUG = 0

for input in f:
  if DEBUG: print(input, end='')
  numbers_only = input
  numbers_only = numbers_only.replace('zero', 'e0e')
  numbers_only = numbers_only.replace('one', 'o1e')
  numbers_only = numbers_only.replace('two', 't2o')
  numbers_only = numbers_only.replace('three', 't3e')
  numbers_only = numbers_only.replace('four', 'f4r')
  numbers_only = numbers_only.replace('five', 'f5e')
  numbers_only = numbers_only.replace('six', 's6x')
  numbers_only = numbers_only.replace('seven', 's7n')
  numbers_only = numbers_only.replace('eight', 'e8t')
  numbers_only = numbers_only.replace('nine', 'n9e')
  numbers_only = re.sub('[^0-9]', '', numbers_only)
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
