# with open("Intermediate\Day 25 - CSV Data and Pandas Library\weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv
import pandas

# with open("Intermediate\Day 25 - CSV Data and Pandas Library\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     next(data_file)
#     for row in data:
#         temperatures.append(int(row[1]))
#     print(temperatures)
    
data = pandas.read_csv("Intermediate\Day 25 - CSV Data and Pandas Library\weather_data.csv")
print(data["temp"])