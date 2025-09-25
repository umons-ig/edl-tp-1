"""
Calculator module - Basic arithmetic operations
Some functions have bugs that need to be fixed!
"""

def add(a, b):
    """Addition of two numbers"""
    return a + b

def subtract(a, b):
    """Subtraction of two numbers"""
    return a - b

def multiply(a, b):
    """Multiplication of two numbers"""
    return a * b

def divide(a, b):
    """Division of two numbers"""
    # Bug: No ZeroDivisionError check
    return a / b

def power(base, exponent):
    """Raise base to the power of exponent"""
    # Bug: Only handles positive exponents, incorrect for 0 and negative
    if exponent == 0:
        return 1
    else:
        result = 1
        for _ in range(exponent):
            result *= base
        return result

def factorial(n):
    """Calculate factorial of n"""
    # Bug: Does not handle negative numbers or 0, 1 correctly
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def average(numbers):
    """Calculate the average of a list of numbers"""
    # Bug: Does not handle empty list
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    print("Calculator Demo")
    print("=" * 20)
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"subtract(10, 4) = {subtract(10, 4)}")
    print(f"multiply(6, 7) = {multiply(6, 7)}")
    print(f"divide(15, 3) = {divide(15, 3)}")
    # These will likely fail or give wrong results with the buggy functions
    # print(f"power(2, 4) = {power(2, 4)}")
    # print(f"factorial(5) = {factorial(5)}")
    # print(f"average([1, 2, 3, 4, 5]) = {average([1, 2, 3, 4, 5])}")
