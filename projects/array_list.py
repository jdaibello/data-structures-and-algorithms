# Calculate average temperature

from array import *

numDays = int(input('How many days temperature? '))
temp = array('f', [])
total = 0

for i in range(numDays):
    nextDay = float(input(f'Day {i + 1}\'s high temp: '))
    temp.append(nextDay)
    total += temp[i]

avg = round(total / numDays, 2)
print(f'\nAverage: {avg}')

above = 0
for i in temp:
    if i > avg:
        above += 1

print(f'{above} day(s) above average')