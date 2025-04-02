def add(a, b):
    """Return the sum of a and b."""
    return a + b
def subtract(a, b):
    """Return the difference of a and b"""
    return a - b
def multiply(a, b):
    """Return the product of a and b"""
    return a * b
def divide(a, b):
    """return the quotient of a and b // Returns error message if b is 0"""
    if b == 0:
        return "Error; not divisible"
    return a / b