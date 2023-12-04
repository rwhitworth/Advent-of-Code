import re

f = open('day3input', 'r')

result = 0
DEBUG = 0
SKIP_CHARS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

# init our default starting state, because we don't want to handle the first
# few lines special
# length of 142 chosen because input file is 140 characters long, and.. see comments further below
lines = {}
lines[0] = lines[1] = lines[2] = '.' * 142

line_counter = -1

for input in f:
  line_counter += 1
  lines[0] = lines[1]
  lines[1] = lines[2]
  # pad the new line with a starting and trailing period
  # this allows us to search on right and left character, even numbers starting or ending the line
  # no algorithm changes needed for initial or ending numbers
  lines[2] = '.' + re.sub('\n', '', input) + '.'

  all_results = re.findall('.*?([0-9]{1,4}).*?', lines[1])

  for res in all_results:
    if DEBUG: print(f"res: {res}\n{lines[0]}\n{lines[1]}")
    num_location = lines[1].find(res)
    # remove res from the input. Some lines (3 in my input) contain duplicate numbers
    lines[1] = lines[1].replace(res, len(res) * '.', 1)
    res_len = len(str(res))
    
    # does the line above have a special character?
    for i in range(-1, res_len+1):
      c = lines[0][i + num_location]
      if c in SKIP_CHARS:
        continue
      if DEBUG: print(f'SPECIAL: {line_counter} {res}')
      result += int(res)
      # don't want to double count it
      break

    # does the line below have a special character?
    for i in range(-1, res_len+1):
      c = lines[2][i + num_location]
      if c in SKIP_CHARS:
        continue
      if DEBUG: print(f'SPECIAL: {line_counter} {res}')
      result += int(res)
      # don't want to double count it
      break

    # does the current line have a special character at either end of the number?
    for i in [num_location - 1, num_location + res_len]:
      c = lines[1][i]
      if c in SKIP_CHARS:
        continue
      if DEBUG: print(f'SPECIAL: {line_counter} {res}')
      result += int(res)
      # don't want to double count it
      break

print(f"result: {result}")
