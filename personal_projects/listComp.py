import random

numbers = [i for i in range(1,10) if i%2==0]


for index, count in enumerate(numbers):
    print(count, index)


temps = [23,54,65,76,34,54,23]
total_temp = 0
avg_temp = 0

for index, temp in enumerate(temps):
    print(temp, "is at index", index)
    total_temp = total_temp + temp
    avg_temp = total_temp / len(temps)

print(f'''
TOTAL TEMPERATURES = {total_temp}
AVERAGE TEMP = {avg_temp}
''')
