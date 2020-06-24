import sys

def menuApp():
  while True:
    print('What would you like to do?\n\t1) Calculate table.\n\t2) Exit.')
    userSelection = int(input('Please choose an option: '))
    checkUserSelection(userSelection)

def checkUserSelection(userSelection):
  if userSelection == 1:
    calculateTable()
  elif userSelection == 2:
    print('Bye.')
    sys.exit()
  else:
    while True:
      userSelection = int(input('Non-valid option. Please choose a valid option: '))
      checkUserSelection(userSelection)

def calculateTable():
  userTableSelection = int(input('Please enter the table to calculate: '))
  for number in range(10):
    number += 1
    numberMultiplied = userTableSelection * (number)
    print(f'{userTableSelection} x {number} = {numberMultiplied}')
  print('\nWhat would you like to do?\n\t1) Calculate other table.\n\t2) Exit.')
  userSelection = int(input('Please choose an option: '))
  checkUserSelection(userSelection)

menuApp()