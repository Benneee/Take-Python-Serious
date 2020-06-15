crypto_prices = {
    "Bitcoin": 40000,
    "Ethereum": 7000,
    "Litecoin": 10
}

# It should be noted that the return values are not lists

# print(crypto_prices.keys())
# print(crypto_prices.values())

for currency in crypto_prices.keys():
    print(currency)

for amount in crypto_prices.values():
    print(amount)