# The enumerate method iterates over a list and keeps track of the index of the item iterated over

errands = [
    "Go to gym",
    "Grab breakfast",
    "Get promoted at work",
    "Sleep"
]
# THe first variable is always the index of the element being iterated over
for i, errand in enumerate(errands):
    print(f"{errand} is the number {i + 1} thing to do on my list today!")

    # OR
for i, errand in enumerate(errands, 1):
    print(f"{errand} is the number {i} thing to do on my list today!")