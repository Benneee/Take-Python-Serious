# Using the with context provides a protective layer over this process
# It performs automatic cleanup, e.g closing the file we open, when the block is done executing
# "r" here is the default processing mode for the open method
# with open("cupcakes.txt", "r") as cupcakes_file:
#     # If a file is massive, it is not advisable to use the read method on it at once
#     print("The file has been opened")
#     # The read method returns a string which we assign to the content variable
#     content = cupcakes_file.read()
#     print(content)

# print("The file has been closed")

# Ask user for file they would like to open
filename = input("What file would you like to open? ")

# Run the open and read operation with the filename they choose to use
with open(filename, "r") as readers_choice:
    print(readers_choice.read())
