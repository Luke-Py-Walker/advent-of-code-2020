filename = 'input.txt'

complements = {}

expenses = []

for expense in open(filename, 'r'):
  complement = 2020 - int(expense)
  if complement in complements:
    print(int(expense)*complements[complement][0]*complements[complement][1])
  else:
    for item in expenses:
      complements[item + int(expense)] = [item, int(expense)]
    expenses.append(int(expense))
