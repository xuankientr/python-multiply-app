#!/usr/bin/env python3
"""
Unit tests for the multiply function
"""

import unittest
from app import multiply


class TestMultiplyFunction(unittest.TestCase):
    """Test cases for the multiply function"""
    
    def test_multiply_positive_integers(self):
        """Test multiply with positive integers"""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(5, 6), 30)
        self.assertEqual(multiply(1, 1), 1)
    
    def test_multiply_with_zero(self):
        """Test multiply with zero"""
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(10, 0), 0)
        self.assertEqual(multiply(0, 0), 0)
    
    def test_multiply_negative_numbers(self):
        """Test multiply with negative numbers"""
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(3, -4), -12)
        self.assertEqual(multiply(-3, -4), 12)
    
    def test_multiply_floats(self):
        """Test multiply with floating point numbers"""
        self.assertAlmostEqual(multiply(2.5, 4), 10.0)
        self.assertAlmostEqual(multiply(3.14, 2), 6.28)
        self.assertAlmostEqual(multiply(0.5, 0.5), 0.25)
    
    def test_multiply_large_numbers(self):
        """Test multiply with large numbers"""
        self.assertEqual(multiply(1000, 1000), 1000000)
        self.assertEqual(multiply(999999, 1), 999999)


if __name__ == "__main__":
    unittest.main()
