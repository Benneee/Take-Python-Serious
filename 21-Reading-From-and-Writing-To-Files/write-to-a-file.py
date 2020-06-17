file_name = "my_first_file.txt"

# "w" here because our processing mode is "write" at this time
with open(file_name, "w") as file_object:
    # The open function creates the file if it does not currently exist in the directory
    # However, if the file does exist, it will overwrite the content of the file, which we might not want
    file_object.write("Hello file \n")
    file_object.write("This is the start of something beautiful!")