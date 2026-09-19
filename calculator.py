"""
Simple Calculator Module
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    print("Add 5 + 3 =", add(5, 3))
    print("Subtract 10 - 4 =", subtract(10, 4))
    print("Multiply 6 * 7 =", multiply(6, 7))
    print("Divide 20 / 4 =", divide(20, 4))
