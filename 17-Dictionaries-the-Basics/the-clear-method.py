# The clear method removes all the elements of list, the same applies to dictionaries
# However, the dictionary object remains in memory

websites = {
    "Google": "https://google.com",
    "Wikipedia": "https://wikipedia.com",
    "Netflix": "https://netflix.com"
}

websites.clear() # This clears the content of the dictionary
print(websites)

del websites # This deletes the dictionary from memory
print(websites)