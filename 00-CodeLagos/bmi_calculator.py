print('Today! We will build a body-mass-index calculator');
print('You only need to tell us your height in metres and weight in kilogram');

print('If you are ready, let us get on with it then!');

print('First, tell us your name');
name = input('Enter your name: ')

weight = float(input('Enter your weight in kilogram (kg): '));
height = float(input('Enter your height in metres (m): '));

print('Your BMI is a fraction of your weight and twice your height');

bmi = weight/(height ** 2);
bmi = round(bmi, 1);

print('Your BMI value is ', bmi);

if bmi < 18.5:
    print('Dear', name, 'you are underweight! Eat some more food and eat right please');
elif bmi > 18.5 and bmi < 25:
    print('Good one', name, 'You have an optimal body-mass-index');
    exit()
elif bmi >= 25 and bmi < 30:
    print('Oh boy, Dear', name, 'Kindly start some exercise!');
    exit()
else:
    print('More exercise please, we do not want you to get too obese!');
    