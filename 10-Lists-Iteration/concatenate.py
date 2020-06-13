def concatenate(strings):
    string_sum = ''
    for s in strings:
        # print(s)
        if len(s) > 2:
            string_sum += s

    return string_sum

print(concatenate(["ab", "cd", "ef", "gh"]))
print(concatenate(["abc", "de", "fgh"]))
print(concatenate(["abcd", "efgh", "ijk"]))
