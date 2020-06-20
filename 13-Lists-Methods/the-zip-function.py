# The zip function returns a list of tuples of elements in similar positions/indexes across multiple lists
breakfast = ['eggs', 'bread', 'tea']
lunch = ['spaghetti', 'sauce', 'sprite']
dinner = ['vegetable soup', 'eba', 'chilled water']

print(list(zip(breakfast, lunch, dinner)))
