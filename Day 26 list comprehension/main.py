numbers = [1, 2, 3]

# without list comprehension
# new_list = []
# for n in numbers:
#     add_n = n + 1
#     new_list.append(add_n)

# new_list = [new_item for item in list]
new_list = [n + 1 for n in numbers]

# You can add a conditional when doing list comprehension
# new_list = [new_item for item in list if test]
odd_numbers = [n for n in numbers if n % 2 != 0]


# Can also do Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# CAREFUL with the syntax, it's key:value and then (key, value)

#Iterate over pandas dictionary
print("Iterate over pandas dictionary")
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)


# loop though a data frame
# for (key,value) in student_data_frame.items():
#     print(value)
#doesn't work that well

# loop through rows of a data frame
# It's helpful to keep the (index, row) format, you can access column data within row eg. row.student, row.score
for (index, row) in student_data_frame.iterrows():
    # print(row)
    # print(row.student)
    # print(row.score)
    if row.student == 'Angela':
        print(row.score)