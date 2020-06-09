from sys import argv

script, filename = argv;

txt = open(filename);

print(f"Here's your file {filename}");

# Read the content of the file 'txt' referenced above
print(txt.read());

print("Type the filename again: ");
file_again = input('> ');

txt_again = open(file_again);
print(txt_again.read());