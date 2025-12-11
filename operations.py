# operations.py
import math

# Basic binary operations
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def power(a, b): return a ** b

def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot modulus by zero.")
    return a % b

# Unary operations
def sqrt(x):
    if x < 0:
        raise ValueError("Square root of negative number not allowed.")
    return math.sqrt(x)

def absolute(x): return abs(x)

# Trigonometric
def sin(x): return math.sin(x)
def cos(x): return math.cos(x)
def tan(x): return math.tan(x)
