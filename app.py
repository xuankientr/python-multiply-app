#!/usr/bin/env python3
"""
Simple Python application with multiply function
"""

def multiply(a, b):
    """
    Multiply two numbers and return the result
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The product of a and b
    """
    return a * b


def main():
    """Main function to demonstrate the multiply function"""
    # Test the multiply function
    result = multiply(3, 4)
    print(f"multiply(3, 4) = {result}")
    
    # Additional examples
    print(f"multiply(5, 6) = {multiply(5, 6)}")
    print(f"multiply(2.5, 4) = {multiply(2.5, 4)}")
    print(f"multiply(-3, 7) = {multiply(-3, 7)}")
    print(f"multiply(10, 10) = {multiply(10, 10)}")  # Demo thêm test case


if __name__ == "__main__":
    main()
