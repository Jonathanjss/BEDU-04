import math
import sys

userBMIList = []

def menuApp():
  print('What would you like to do?\n\t1) Calculate BMI.\n\t2) View BMI history.\n\t3) Exit.')
  userSelection = int(input('Please choose an option: '))
  checkUserSelection(userSelection)

def checkUserSelection(userSelection):
  if userSelection == 1:
    calculateBMI()
  elif userSelection == 2:
    showBMIHistory()
  elif userSelection == 3:
    print('Bye.')
    sys.exit()
  else:
    userSelection = int(input('Non-valid option. Please enter a valid option: '))
    checkUserSelection(userSelection)

def calculateBMI():
  name = input('Please enter a name: ')
  height = float(input('Please enter the height in meters: '))
  weight = float(input('Please enter the weight in kilograms: '))
  userBMI = weight/(math.pow(height, 2))
  if userBMI < 18.5:
    weightStatus = 'underweight'
    print(f'You have a BMI of {userBMI}, then your weight status is {weightStatus}.')
  elif userBMI >= 18.5 and userBMI < 24.9:
    weightStatus = 'healthy'
    print(f'You have a BMI of {userBMI}, then your weight status is {weightStatus}.')
  elif userBMI >= 24.9 and userBMI < 29.9:
    weightStatus = 'overweight'
    print(f'You have a BMI of {userBMI}, then your weight status is {weightStatus}.')
  else:
    weightStatus = 'obese'
    print(f'You have a BMI of {userBMI}, then your weight status is {weightStatus}.')
  getBMIUser(name, userBMI, weightStatus)
  userSelection = int(input('\nPlease choose an option:\n\t1) Calculate other BMI.\n\t2) Check BMI history.\n\t3) Exit.\nOption: '))
  checkUserSelection(userSelection)

def getBMIUser(name, userBMI, weightStatus):
  userBMIData = {
    "name": name,
    "userBMI": userBMI,
    "weightStatus": weightStatus
  }
  userBMIList.append(userBMIData)

def showBMIHistory():
  print('\n---------------BMI History---------------')
  if len(userBMIList) > 0:
    for user in userBMIList:
      for userKey in user.keys():
        if userKey == 'name':
          print(f'Name: {user[userKey]}')
        elif userKey == 'userBMI':
          print(f'BMI: {user[userKey]}')
        else:
          print(f'Weight status is {user[userKey]}.\n-----------------------------------------')
    print('\n')
    menuApp()
  else:
    print('The list is empty.')

menuApp()