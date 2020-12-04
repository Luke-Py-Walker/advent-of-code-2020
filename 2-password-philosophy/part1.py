filename = 'input.txt'

valid_passwords = 0

for password in open(filename, 'r'):
  parsed = password.split()

  letter_range = parsed[0].split('-')
  letter_min = int(letter_range[0])
  letter_max = int(letter_range[1])

  given_letter = parsed[1][0]
  given_letter_count = 0

  for letter in parsed[2]:
    if letter == given_letter:
      given_letter_count += 1

  if given_letter_count >= letter_min and given_letter_count <= letter_max:
    valid_passwords += 1

print(valid_passwords)
