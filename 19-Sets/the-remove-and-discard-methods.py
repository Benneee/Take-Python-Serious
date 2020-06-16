# The remove method raises a KeyError if the item being looked for isn't found
# The discard method doesn't

agents = { "Mulder", "Scully", "Doggett", "Reyes" }
agents.remove("Doggett")
# removed = agents.remove("Doggett")
print(agents)
# print(removed) # Returns None

# agents.remove("Skinner") # Raises KeyError: 'Skinner'

# discarded = agents.discard('Reyes')
agents.discard('Reyes')
print(agents)
# print(discarded) # Returns None
agents.discard("Skinner") # No error is thrown