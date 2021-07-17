# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# import os

# cwd = os.getcwd()  # get the cuent working directory (cwd)
# files = os.listdir(cwd)  # get all the files in that directory
# print("Files in %r: % s" % (cwd, files))


# with open('Day 25/weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
data = pandas.read_csv('Day 25/weather_data.csv')
print(type(data))
