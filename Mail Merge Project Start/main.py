# TODO: Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as source_letter:
    letter = source_letter.read()


def write_letter(input_name):
    new_letter = letter.replace("[name]", input_name)
    return new_letter


# for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()
    for name in names_list:
        cleaned_name = name.replace("\n", "")
        with open(f"./Output/ReadyToSend/{cleaned_name}_invitation", mode="w") as new_inv:
            new_inv.write(write_letter(cleaned_name))

# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
