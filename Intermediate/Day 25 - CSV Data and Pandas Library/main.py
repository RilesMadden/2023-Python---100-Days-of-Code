import pandas
    
data = pandas.read_csv("Intermediate\Day 25 - CSV Data and Pandas Library\weather_data.csv")
print(data)
# data_dict = data.to_dict()
# print(data_dict)

# # # temp_list = data["temp"].to_list()
# # # print(temp_list)

# # # average_temp = sum(temp_list) / len(temp_list)
# # # print(average_temp)

# # # print(data["temp"].max())
# # # print(data.temp)

# # #get data in rows
# # print(data[data.day == "Monday"])

# # #get data row where temp = max
# # print(data[data.temp == data.temp.max()])

# # # Convert Monday's temperature to Fahrenheit
# # monday = data[data.day == "Monday"]
# # print((monday.temp * (9/5) + 32))

# #Convert dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# # make csv file
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")