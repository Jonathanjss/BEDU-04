import math
print('This is a little program that allows you to know your BMI.')
height = float(input('Please enter your height in meters: '));
weight = float(input('Please enter your weight in kilograms: '));
userBMI = float(format(weight/(math.pow(height,2)),'.2f'))

if userBMI < 18.5:
  print(f'You have a BMI of {userBMI} so you are underweight.')
elif userBMI >= 18.5 and userBMI < 25:
  print(f'Congrats! You have a BMI of {userBMI} so you are healthy.')
elif userBMI >= 25 and userBMI < 30:
  print(f'You have a BMI of {userBMI} so you are overweight, do exercise.')
elif userBMI >= 30 and userBMI < 40:
  print(f'You have a BMI of {userBMI} so you are obese, please go to the doctor.')
else:
  print(f'You have a BMI of {userBMI} so you are a high risk person, please go to the doctor.')
