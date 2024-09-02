# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#


import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row)

temperatures = []
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        if row != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)