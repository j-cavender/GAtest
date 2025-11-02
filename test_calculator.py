import unittest


class TestCalculator(unittest.TestCase):
    """Unit tests for a simple calculator"""
    
    def test_add_two_positive_numbers(self):
        """Test addition of two positive numbers"""
        result = Calculator().add(2, 3)
        self.assertEqual(result, 5)
    
    def test_add_positive_and_negative(self):
        """Test addition of positive and negative number"""
        result = Calculator().add(5, -3)
        self.assertEqual(result, 2)
    
    def test_add_two_negative_numbers(self):
        """Test addition of two negative numbers"""
        result = Calculator().add(-2, -3)
        self.assertEqual(result, -5)
    
    def test_subtract_two_positive_numbers(self):
        """Test subtraction of two positive numbers"""
        result = Calculator().subtract(5, 3)
        self.assertEqual(result, 2)
    
    def test_subtract_negative_from_positive(self):
        """Test subtracting a negative number"""
        result = Calculator().subtract(5, -3)
        self.assertEqual(result, 8)
    
    def test_multiply_two_positive_numbers(self):
        """Test multiplication of two positive numbers"""
        result = Calculator().multiply(4, 3)
        self.assertEqual(result, 12)
    
    def test_multiply_by_zero(self):
        """Test multiplication by zero"""
        result = Calculator().multiply(5, 0)
        self.assertEqual(result, 0)
    
    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers"""
        result = Calculator().multiply(-3, -4)
        self.assertEqual(result, 12)
    
    def test_divide_two_positive_numbers(self):
        """Test division of two positive numbers"""
        result = Calculator().divide(10, 2)
        self.assertEqual(result, 5)
    
    def test_divide_with_decimal_result(self):
        """Test division resulting in decimal"""
        result = Calculator().divide(7, 2)
        self.assertEqual(result, 3.5)
    
    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises an error"""
        with self.assertRaises(ValueError):
            Calculator().divide(5, 0)


if __name__ == '__main__':
    unittest.main()
