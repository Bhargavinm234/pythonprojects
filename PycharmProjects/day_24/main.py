# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#     #not required = file.close()
#
#
# with open("my_file.txt", mode="w") as file1:
#     file1.write("\nnewwwww txtt")

# with open("new_file.txt",mode="w") as files:
#     files.write("Hii\nByeee")

with open("/Users/DELL/Desktop/new_file.txt") as file:
    contents = file.read()
    print(contents)

with open("../../Desktop/new_file.txt") as file:
    contents = file.read()
    print(contents)

