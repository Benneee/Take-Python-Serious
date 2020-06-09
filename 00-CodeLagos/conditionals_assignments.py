# A program to test if the length of a string is greater 

# Collect input from the user
sample_string = input('Enter your name: ');

str_length = len(sample_string);
if str_length > 5:
    print('Your name, ',sample_string,', is longer than 5 letters');
elif str_length == 5:
    print('Yay! Your name, ',sample_string,' ,is exactly 5 letters');
else:
    print('Your name, ',sample_string,', is lesser than 5 letters');



# A program to test if a number is odd
print("Let's play a game of odd numbers, enter a number and I will tell you if it is an odd number");
user_entry = input('Enter your number: ');
entry = float(user_entry);

if entry % 2 != 0:
    print('Yay! Your number', user_entry, 'is an odd number');
else:
    print('Sorry, your number is not an odd number');


# A program to check if a year is a leap year
# Checks
print("Let's check if you were born in a leap year");
sample_year = input('Enter your year of birth: ');
check1 = int(sample_year) % 400;
check2 = int(sample_year) % 4;

if check1 == 0:
    print('Yay! You were born in a leap year');
elif check2 == 0:
    print('Yay! you were born in a leap year');
else:
    print('Aww! You were not born in a leap year');