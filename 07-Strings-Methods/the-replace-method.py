# THe replace method repplaces all the occurrences of the substring of a string with another string
# It collects two parameter, the substring to replace and the replacing substring

phone_number = "234 818 437 5940"

formatted_pn = phone_number.replace(" ", "-");

print(formatted_pn);

# Replace doesn't mutate the original string, it simply provides us with a new string

# Practice thingy
def fancy_cleanup(word):
    letters = word.strip().replace("g", "z").replace(" ", "!")
    return letters

list_of_words = ["       geronimo crikey        ", "        nonsense          ", "grade"];

# Loop through the list and run the fancy_cleanup method on each of the words in the list
# Return the words in a new array
formatted_list = []

for word in list_of_words:
    formatted = fancy_cleanup(word)
    formatted_list.append(formatted);

print(formatted_list);
    