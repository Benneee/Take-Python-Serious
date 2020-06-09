from math import pi;

print('Let us find the area of a circle');

print('For a circle, we will need a value for the radius of the circle');

print('The formula to get the are of a circle is pi * radius ** 2')

radius = input('Enter the radius of your circle: ');
area_of_circle = pi * (float(radius) ** 2);

area = round(area_of_circle, 3);

print('Area of the circle is: ', area);