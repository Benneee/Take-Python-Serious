# Filters come after the for-loop in the list comprehension syntax

donuts = [
    "Boston Cream",
    "Jelly",
    "Vanilla Cream",
    "Glazed",
    "Chocolate Cream"
]

creamy_donuts = [donut for donut in donuts if "Cream" in donut]

remove_creamy =  [donut.split(" ")[0] for donut in donuts if "Cream" in donut]
print(remove_creamy);