filename = 'input.txt'

expenses = {}

for expense in open(filename, 'r'):
  complement = 2020 - int(expense)
  if complement in expenses:
    print(complement*(2020-complement))
  else:
    expenses[int(expense)] = 1
