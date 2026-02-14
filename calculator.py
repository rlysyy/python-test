#!/usr/bin/env python3
"""
Calculator Module
Basic arithmetic operations.
"""

def add(a, b):
    """Addition"""
    return a + b

def subtract(a, b):
    """Subtraction"""
    return a - b

def multiply(a, b):
    """Multiplication"""
    return a * b

def divide(a, b):
    """Division"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    """Power"""
    return a ** b

def modulo(a, b):
    """Modulo"""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b

def calculate(expression):
    """Parse and calculate a simple expression"""
    try:
        return eval(expression)
    except Exception as e:
        raise ValueError(f"Invalid expression: {expression}")

if __name__ == "__main__":
    print("Simple Calculator")
    print("Operations: +, -, *, /, **, %")
