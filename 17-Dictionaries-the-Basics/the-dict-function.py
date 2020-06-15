# A valid input to the dict method is a list of lists
# The internal lists must contain two elements as these elements make up the key-value pair of the dictionary to be created

employee_titles = [
    ["Mary", "Brand Manager"],
    ["Brian", "Vice President"],
    ["Brandon", "President"]
]

new_dict = dict(employee_titles)

print(new_dict);