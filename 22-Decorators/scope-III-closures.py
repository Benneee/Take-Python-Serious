# A closure is a programming pattern in which a scope retains access to an enclosing scope's names

def outer():
    candy = "Snickers"

    def inner():
        return candy

    return inner()