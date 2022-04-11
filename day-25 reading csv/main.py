# # import csv
# #
# # with open("weather_data.csv", newline="") as weather_data:
# #     data = csv.reader(weather_data)
# #     temperatures = []
# #     next(data, None)
# #     for row in data:
# #         temperatures.append(int(row[1]))
# #     print(temperatures)
#
# def c_to_f(c_temp):
#     f_temp = c_temp * 1.8 + 32
#     return f_temp
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data['temp'])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# # Getting data from columns
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(f'The average temperature is: {data["temp"].mean()}')
# print(f'The maximum temperature is: {data["temp"].max()}')  # or data.temp.max()
#
# # Getting data from rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
#
# print(c_to_f(int(monday.temp)))
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# student_scores = pandas.DataFrame(data_dict)
# student_scores.to_csv("New_data.csv")
#
# # temp_list_average = 0
# # for temp in temp_list:
# #     temp_list_average += temp
# # temp_list_average = round(temp_list_average / len(temp_list), 1)
# # print(f"The average temperature is {temp_list_average}")
#

# Time to analyze some squirrel data
import pandas

squirrel_data = pandas.read_csv("squirrel_count.csv")
fur_color = squirrel_data["Primary Fur Color"]

fur_counts = fur_color.value_counts()


data_dict = {
    "Fur Colour": fur_color.unique().tolist(),
    "Count": fur_counts.to_list()
}
data_dict["Fur Colour"].pop(0)  # To get rid of the nan
print(data_dict)
squirrel_color_counts = pandas.DataFrame(data_dict)
squirrel_color_counts.to_csv("fur_colour_count.csv")


