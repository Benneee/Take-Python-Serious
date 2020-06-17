# The most efficient approach to reading a file is by reading it line by line 
# especially when the file is massive

# The file returned by the read() method is actually an iterable so we can traverse it by using a for-loop

with open("cupcakes.txt") as cupcakes_file:
    for line in cupcakes_file:
        print(line)