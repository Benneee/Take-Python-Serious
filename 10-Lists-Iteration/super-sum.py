def super_sum(strings):
    # Return the sum of the index of 's' in the elements of the string in the list
    s_total = 0
    for s in strings:
        s_total += s.find('s');
    
    return s_total


print(super_sum([]))
print(super_sum(["mustache", "pessimist"]))
print(super_sum(["mustache", "greatest", "almost"]));