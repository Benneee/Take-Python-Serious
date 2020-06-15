flight_prices = {
    "Kaduna": 14000,
    "Delta": 8000,
    "Maiduguri": 20000
}

# The key difference here is that the access-by-key method throws an error (KeyError) when the key it seeks is not available
# However, the get method allows us to pass an alternative object to be returned if the key isn't present or returns None if we don't provide an alternative object to be returned

print(flight_prices["Kaduna"])
# print(flight_prices["Kadun"]) # Throws a KeeyError

print(flight_prices.get("Kaduna", 15000))
print(flight_prices.get("Kadun", 15000)) # Returns 15000 instead because there is no key known as Kadun
print(flight_prices.get("Kadun")) # Returns None since no default value is provided
