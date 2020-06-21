print('This is a little program to know the times table of a number.')
number = int(input('Please insert a number: '))
print(f'The times table for the number {number} is: ')

for num in range(10):
  print(f'{number}*{num+1} = {number*(num+1)}')