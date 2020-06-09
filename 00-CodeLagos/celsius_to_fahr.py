print('Hello there! Let us convert our temperature values from Celsius to Fahrenheit');

print('To get this done, I will need your celsius value, then run it through the formula shown below');

print('F = (0°C × 9/5) + 32');

cel_value = input('Enter value for the temperature in Celsius: ');

fahr_value = round((float(cel_value) * (9/5)) + 32, 3);

print('The value of', str(cel_value)+ '°C', 'in Fahrenheit is: ', str(fahr_value) + '°F');