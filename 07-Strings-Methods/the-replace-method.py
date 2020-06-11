# THe replace method repplaces all the occurrences of the substring of a string with another string
# It collects two parameter, the substring to replace and the replacing substring

phone_number = "234 818 437 5940"

formatted_pn = phone_number.replace(" ", "-");

print(formatted_pn);

# Replace doesn't mutate the original string, it simply provides us with a new string