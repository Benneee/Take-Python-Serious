from sys import argv

script, input_file = argv

# Create a function to read the input file
def print_all(f):
    print(f.read())

# The seek method deals with bytes and not lines, so when the method is called,
# It takes the file back to 0 bytes
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First, let's print the whole file:\n")

print_all(current_file);

print("Now, let's rewind like it's a tape!")

rewind(current_file)

print("Let's print three lines");

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)