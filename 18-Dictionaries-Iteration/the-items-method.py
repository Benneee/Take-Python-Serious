# The items methods return an iterable view object
# For each iteration, it provides us with a two-element tuple which is a collection of the key and its value
# The output can be stored in variables in the process

college_courses = {
    "Science": "Mr Osuchukwu",
    "Mathematics": "Mr Adeleye",
    "English": "Mrs Osudi"
}

for subject, teacher in college_courses.items():
    print(f"The subject {subject} is being taught by {teacher}.")

# Use an "_" underscore if you need to ignore the key or value in the iteration.