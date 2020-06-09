# Area of triangle
print('Hiya! Let us calculate the area of a triangle');

print("A triangle's area can be calculated using the formula: 1/2 * base * height");

print("Kindly provide us with your respective values for base and height");

# Collect the values for base and height from users
base = input('Enter the number for base of the triangle: ');
height = input('Enter the number for height of the triangle: ');

triangle_area = 0.5 * float(base) * float(height);

print('Area of your triangle is: ', triangle_area);