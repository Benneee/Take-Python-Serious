from sys import argv;

# Pass values to the script when you run it in the command line
# e.g python3 command_line.py rice ik amaka
# As you can see, we only pass values for the last 3 variables as the script is a recognized keyword
script, first, second, third = argv;

print(f'The script is called {script} ');
print(f'Your best food is {first}')
print(f'Your other name is {second}')
print(f"Your sister's name is {third}")