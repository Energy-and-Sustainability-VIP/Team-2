import csv
with open("Assignment-1-raw-data.csv", 'r') as f: #opens file
    data = list(csv.reader(f, delimiter=','))


import numpy as np
data = data[1:]
readings  = []
for i in range(0, len(data)): #obtains reading data
    reading = data[i][2]
    if reading != "":
        reading_float_no_spaces = float(reading.replace(" ", ""))
        readings.append(reading_float_no_spaces)
    else:
        readings.append(0)

readings = np.array(readings) #Maximum calculation
max_location = np.argmax(readings)
print("Max: ", data[max_location])

min = 10000000000 #Minimum calculation
for i in range(0, len(data)):
    if readings[i] != 0 and readings[i] < min:
        min = readings[i]
        min_location = i
print("Min: ", data[min_location])

sum = 0 #Average calculation
count = 0
for i in range(0, len(data)):
    if readings[i] != 0:
        sum += readings[i]
        count += 1
avg = sum/count
print("Avg: ", f"{avg:.2f}")

import pandas as pd
assignment_1_df = pd.read_csv('Assignment-1-raw-data.csv')
assignment_1_df['watts'] = assignment_1_df['meter_reading'] * 1000 * 4
assignment_1_df['kwh'] = assignment_1_df['meter_reading']

assignment_1_df.to_csv('AssignmentOne.csv', index = False)

