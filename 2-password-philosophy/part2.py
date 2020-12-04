filename = 'input.txt'

valid_passwords = 0

for password in open(filename, 'r'):
  parsed = password.split()

  letter_range = parsed[0].split('-')
  letter_pos1 = int(letter_range[0]) - 1
  letter_pos2 = int(letter_range[1]) - 1

  given_letter = parsed[1][0]

  password = parsed[2]

  valid_pos1 = letter_pos1 >= 0 and letter_pos1 < len(password) and password[letter_pos1] == given_letter
  
  valid_pos2 = letter_pos2 >= 0 and letter_pos2 < len(password) and password[letter_pos2] == given_letter

  if valid_pos1 != valid_pos2:
    valid_passwords += 1

print(valid_passwords)
