print('Let us play with some temperature units');

far_input = input('Enter a temperature value in Fahrenheit: ');
far_value = float(far_input);

cel_value = (far_value - 32) * (5/9);
print("Here's your temperatue in Celsius: ", str(cel_value)+'°C');