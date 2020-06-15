words = ["danger", "beware", "danger"]
# Create a dictionary containing the value of count of the elements in the words list

def count_words(strings):
    counts = {}
    for word in strings:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


counts = count_words(words)
# print(counts);

def to_dict(the_list):
    the_dict = {}
    for index, value in enumerate(the_list):
        the_dict[value] = index

    return the_dict

detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
new_dict = to_dict(detectives)    
# print(new_dict)


def length_counts(the_list):
    the_dict = {}
    count = 1;
    for value in the_list:
        if len(value) in the_dict:
            the_dict[len(value)] += count
        else:
            the_dict[len(value)] = count

    return the_dict

print(length_counts(["Brazil", "Argentina", "Venezuela", "Ecuador", "Bolivia", "Peru"]));
