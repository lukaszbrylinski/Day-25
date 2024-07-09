# with open("weather_data.csv") as file:
#     data = file.readlines()

# import csv
#
# temperatures = []
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     print(data)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# print(data)
# data_dict = data.to_dict()
# data_list = data["temp"].to_list()
# # print(sum(data_list)/len(data_list))
# print(data["temp"].max())
# # Get column
# print(data["condition"])
# print(data.condition)

#Get row

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 1.8 +32
# print(monday_temp_F)
# print((int(monday["temp"]) * 1.8 + 32))
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey = sum(data["Primary Fur Color"] == "Gray")
black = sum(data["Primary Fur Color"] == "Black")
cinnamon = sum(data["Primary Fur Color"] == "Cinnamon")
data_dict = {
    "Fur Color" : ["Gray", "Black", "Cinnamon"],
     "Count": [grey, black, cinnamon]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
print(df)
