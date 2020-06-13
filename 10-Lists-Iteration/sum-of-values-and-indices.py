def sum_of_values_indices(values):
    if len(values) == 0:
        return 0
    values_sum = 0
    indices_sum = 0
    total = 0;
    for index, value in enumerate(values):
        indices_sum += index
        values_sum += value
        total = indices_sum + values_sum
    
    return total;
        

print(sum_of_values_indices([1, 2, 3]))
print(sum_of_values_indices([0, 0, 0, 0]))
print(sum_of_values_indices([]))