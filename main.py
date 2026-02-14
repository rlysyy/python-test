#!/usr/bin/env python3
"""
Python Test Project
A simple test project for OpenClaw demonstration.
"""

def hello_world():
    """Print a greeting message."""
    print("Hello, World!")
    print("Welcome to Python Test Project!")


def calculate_sum(a, b):
    """Calculate the sum of two numbers."""
    return a + b


def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib


def main():
    """Main function to demonstrate basic operations."""
    print("=" * 50)
    print("Python Test Project")
    print("=" * 50)
    
    # Hello
    hello_world()
    print()
    
    # Calculate sum
    a, b = 10, 20
    print(f"Sum of {a} + {b} = {calculate_sum(a, b)}")
    print()
    
    # Fibonacci
    n = 10
    print(f"First {n} Fibonacci numbers:")
    print(fibonacci(n))
    print()
    
    print("Project demonstration complete!")


if __name__ == "__main__":
    main()
