salutation = "Mr. Kermit the Frog"

# The startswith method looks for a substring at/from the beginning of the original
# The endswith method looks for a substring at/from the end of the original
print(salutation.startswith("Mr"));
# startswith and endswith are case-sensitive

print(salutation.startswith("m")); # False

print(salutation.endswith("og"))