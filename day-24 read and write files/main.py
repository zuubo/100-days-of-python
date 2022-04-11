with open("../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)


# # to write, make sure to change open mode, it'll open as read-only by default
# with open("my_file.txt", mode="w") as file:
#     file.write("New text")  # this will overwrite whatever was in the file

# can use mode="a" to append new stuff
# with open("my_file.txt", mode="a") as file:
#     for _ in range(10):
#         file.write("\nnew text")