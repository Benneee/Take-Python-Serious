# While immutable lists are tuples, a frozen set is an immutable set
# When values are added to a frozen set, they are set in place.
chocolates = [ "Mars", "Snickers", "Milky Way" ]
mr_freeze = frozenset(chocolates) # collects an iterable

print(mr_freeze);chocolates = { "Mars", "Snickers", "Milky Way" }

regular_set = { 1, 2, 3 }
# print({regular_set: "Some value"}) # This will throw an error of unhashable type: 'set'

# However
regular_set = frozenset(regular_set)
print(regular_set)