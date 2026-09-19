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

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

if __name__ == "__main__":
    print("Add 5 + 3 =", add(5, 3))
    print("Subtract 10 - 4 =", subtract(10, 4))
    print("Multiply 6 * 7 =", multiply(6, 7))
    print("Divide 20 / 4 =", divide(20, 4))
    print("Factorial 5! =", factorial(5))
    print("Fibonacci 7 terms =", fibonacci(7))
