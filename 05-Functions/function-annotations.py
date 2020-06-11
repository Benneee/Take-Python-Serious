# If we are being honest my guy, this thing is technically useless
def tryMoreStuff(x: int, y: str) -> str:
    print(f"There are {x} {y}")

tryMoreStuff(5, 'mangoes')

# Annotation simply means labelling stuff
# The way it works here is that any other dev that picks this up knows what type of value to send in as parameters
# However, if we do send in wrong data types, no error will be thrown, hence my first statement.
# It's basically just dope for documentation