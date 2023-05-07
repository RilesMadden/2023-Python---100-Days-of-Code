# Create csv file which states fur color and count of squirres
import pandas


# data_csv = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data_csv)

# import csv data
data_csv = pandas.read_csv("Intermediate\Day 25 - CSV Data and Pandas Library\Squirrel Census Data Analysis\squirrel_data.csv")

# extract the fur color series, and then count
color_list = data_csv["Primary Fur Color"].to_list()
# print(color_list)
gray_count = color_list.count('Gray')
red_count = color_list.count('Cinnamon')
black_count = color_list.count('Black')

color_dict = {
    "colors": ['gray', 'red', 'black'],
    "count": [gray_count, red_count, black_count]
}

color_df = pandas.DataFrame(color_dict)
color_df.to_csv('Intermediate\Day 25 - CSV Data and Pandas Library\Squirrel Census Data Analysis\color_count.csv')

# gray_squirrels = data_csv[data_csv["Primary Fur Color"] == 'Gray']
# count_gray = len(gray_squirrels)
# print(count_gray)