def in_list(words, word):
    position = -1
    for index, s in enumerate(words):
        if s == word:
            position = index

    return position

strings = ["enchanted", "sparks fly", "long live"];
print(in_list(strings, "enchanted"))
print(in_list(strings, "long live"))