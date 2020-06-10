# For loop
the_count = [1, 2, 3, 4, 5, 6];

fruits = ['apples', 'oranges', 'pears', 'apricots'];

for num in the_count:
    print(f"We just hit {num}")

for f in fruits:
    print(f"Let's eat {f}")


# While loop
x = 0;
numbers = [];

while x < 6:
    numbers.append(x)
    
    x = x + 1
    print("Numbers now: ", numbers)

print('The numbers: ');

for val in numbers:
    print(val)


# Play thing
def testStuff(value):
    array_of_values = [];
    while value < 10:
        array_of_values.append(value)
        value = value + 1

    return array_of_values

fullArray = testStuff(3)
print('array: ', fullArray)