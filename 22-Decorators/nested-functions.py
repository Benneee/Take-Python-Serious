# Gallons to cups

# 1 gallon = 4 quarts
# 1 quart = 2 pints
# 1 pint = 2 cups

def convert_gallons_to_quarts(gallons):
    def gallons_to_quarts(gallons):
        print(f"Converting {gallons} gallons to Quarts")
        return gallons * 4

    def quarts_to_pints(quarts):
        print("Converting {quarts} quarts to pints")
        return quarts * 2

    def pint_to_cups(pints):
        print(f"Converting {pints} pints to cups")
        return pints * 2

    quarts = gallons_to_quarts(gallons)
    pints = quarts_to_pints(quarts)
    cups = pint_to_cups(pints)

    return cups


print(convert_gallons_to_quarts(3))