# The processing mode to append to a file is "a"

# If the file we want to edit does not exist, the file will be created and we can continuously append to it
with open("my_first_file.txt", "a") as file_object:
    file_object.write("\n The continuation of something amazing!")
