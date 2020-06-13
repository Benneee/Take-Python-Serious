def sum_of_length(a_list):
    if len(a_list) == 0:
        return None
    else:
        sum_of_a = 0
        for a in a_list:
            sum_of_a = sum_of_a + len(a)
        return sum_of_a
    
print(sum_of_length(["Hello", "Bob", "How"]))
