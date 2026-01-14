# with open("./weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#
# print(data)

# import csv
# with open("./weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))
#
# print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")

# print(data["temp"])

# data_dict = data.to_dict()
# # print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# print(data["temp"].mean())

# print(data["temp"].max())

# # Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in row
# print(data[data.day == "Monday"])

# Print row with highest temprature
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp*9/5+32)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# The Great Squirrel Census Data Analysis
import pandas as pd

# My solution
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_list = data['Primary Fur Color'].value_counts().index
count_list = data['Primary Fur Color'].value_counts().values

new_data = pd.DataFrame({
    "Fur Color": color_list,
    "Count": count_list
})

print(new_data)
new_data.to_csv("squirrel_count.csv")

# Other better solutions
# new_data = data['Primary Fur Color'].value_counts().reset_index()
# new_data.columns = ['Fury color', 'Count']
# print(new_data)

# count = data.groupby(["Primary Fur Color"]).size().reset_index(name='Count').to_csv("squirrel_count.csv")



