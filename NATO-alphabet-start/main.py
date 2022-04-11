import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
#
# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alph = {row.letter:row.code for (index, row) in data.iterrows()}

# for (letter, code) in nato_alph.items():
#     print(code)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("What do you want to NATOfy?: ").upper()
input_as_list = [char for char in user_input]  # don't actually need this list
natofied_list = [nato_alph[char] for char in input_as_list]  # could've used as source list here
# for char in input_as_list:
#     if char in nato_alph.keys():
#         natofied_list.append(nato_alph[char])
print(natofied_list)
