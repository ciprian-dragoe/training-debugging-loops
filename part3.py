choice = input('Enter a letter: ')

while True:
  if len(choice) == 0 or choice == ' ' or len(choice) > 1:
    choice = input('Enter a letter: ')
  else:
    break

print('program finishes')